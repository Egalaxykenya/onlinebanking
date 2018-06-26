from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from bankingapp.models import UtilityPayment, FundsTransfer, UserProfile, UserBankAccount
from django.contrib.auth import authenticate, login
from bankingapp.forms import LoginForm
from django.contrib.auth.decorators import login_required

#paginator combiner imports
from itertools import chain

def getuser(request):
    loggeduser = None
    userid = None
    isadmin = None
    if request.user.is_authenticated():
        loggeduser = request.user.username
        userid = request.user.id
        isadmin = request.user.is_superuser
    return loggeduser, userid, isadmin

def index(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleanedform = form.cleaned_data
            user = authenticate(username=cleanedform['username'], password=cleanedform['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'bankingapp/home.html', context = context_dict )
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    context_dict = { 'form': form}

    return render(request, 'bankingapp/index.html', context=context_dict)


@login_required
def apphome(request):
    loggeduser, userid, isadmin = getuser(request)

    userpersonaldetails = UserProfile.objects.filter(id=userid)
    useraccountdetails = UserBankAccount.objects.filter(accountID=userid)

    context_dict = {'loggeduser': loggeduser, 'userpersonaldetails':userpersonaldetails, 'useraccountdetails': useraccountdetails }


    return render(request, 'bankingapp/home.html', context = context_dict )

@login_required
def fundstransactions(request):
    loggeduser, userid, isadmin = getuser(request)
    if isadmin:
        fundstransfers = FundsTransfer.objects.all()
        fundstransferpaginator = Paginator(fundstransfers, 10) # List up to 10 fundstransfer transactions
        page = request.GET.get('page')

        try:
            transfers = fundstransferpaginator.page(page)
        except PageNotAnInteger:
            transfers = fundstransferpaginator.page(1)
        except EmptyPage:
            transfers = fundstransferpaginator.page(paginator.num_pages)
    else:

        fundstransfers = FundsTransfer.objects.filter(transferID_id=userid)
        fundstransferpaginator = Paginator(fundstransfers, 10) # List up to 10 fundstransfer transactions
        page = request.GET.get('page')

        try:
            transfers = fundstransferpaginator.page(page)
        except PageNotAnInteger:
            transfers = fundstransferpaginator.page(1)
        except EmptyPage:
            transfers = fundstransferpaginator.page(paginator.num_pages)

    context_dict = {'loggeduser':loggeduser, 'transfers':transfers, 'page':page }

    return render(request, 'bankingapp/fundstransactions.html', context= context_dict)

@login_required
def utilitybillstransactions(request):
    loggeduser,userid, isadmin = getuser(request)
    if isadmin:
        utilitybills = UtilityPayment.objects.all()
        billspaginator = Paginator(utilitybills, 10)
        page = request.GET.get('page')
        try:
            bills = billspaginator.page(page)
        except PageNotAnInteger:
            # if page is not an integer deliver the first page
            bills = billspaginator.page(1)
        except EmptyPage:
            # if page is out of range deliver last page of the results
            bills = billspaginator.page(paginator.num_pages)
    else:

        utilitybills = UtilityPayment.objects.filter(customerName_id=userid)
        billspaginator = Paginator(utilitybills, 10) # List 10 utility bills per page
        page = request.GET.get('page')
        try:
            bills = billspaginator.page(page)
        except PageNotAnInteger:
            # if page is not an integer deliver the first page
            bills = billspaginator.page(1)
        except EmptyPage:
            # if page is out of range deliver last page of the results
            bills = billspaginator.page(paginator.num_pages)
    context_dict = {'loggeduser': loggeduser, 'bills':bills, 'page':page}

    return render(request, 'bankingapp/utilitybillstransactions.html', context=context_dict)

@login_required
def monthlystatements(request):
    loggeduser, userid, isadmin = getuser(request)
    if isadmin:
        #if logged in user is admin, do not access commit transaction or account balance page

        context_dict = {'loggeduser':loggeduser, 'firstname': request.user.first_name, 'lastname': request.user.last_name}

        return render(request, 'bankingapp/admininfo.html', context=context_dict)
    else:
        bankaccountdetails = UserBankAccount.objects.filter(accountID=userid)
        context_dict = {'loggeduser': loggeduser, 'bankaccountdetails':bankaccountdetails }

        return render(request, 'bankingapp/monthlystatements.html', context=context_dict)


@login_required
def fundstransfer(request):
    loggeduser, userid, isadmin = getuser(request)
    if isadmin:
        context_dict = {'loggeduser':loggeduser, 'firstname': request.user.first_name, 'lastname': request.user.last_name}
        return render(request, 'bankingapp/admininfo.html', context=context_dict)
    else:
        context_dict = {'loggeduser': loggeduser }


        return render(request, 'bankingapp/fundstransfer.html', context=context_dict)


@login_required
def payutilities(request):
    loggeduser,userid, isadmin = getuser(request)
    if isadmin:
        context_dict = {'loggeduser':loggeduser, 'firstname': request.user.first_name, 'lastname': request.user.last_name}
        return render(request, 'bankingapp/admininfo.html', context=context_dict)
    else:

        context_dict = {'loggeduser':loggeduser}

        return render(request, 'bankingapp/payutilities.html', context = context_dict)

@login_required
def updateprofile(request):
    loggeduser, userid, isadmin = getuser(request)

    if isadmin:
        context_dict = {'loggeduser': loggeduser }
        return render(request, 'bankingapp/adminupdateprofile.html', context = context_dict)
    else:
        context_dict = {'loggeduser': loggeduser }
        return render(request, 'bankingapp/updateprofile.html', context = context_dict)

@login_required
def accesslogs(request):
    loggeduser, userid, isadmin = getuser(request)
    if isadmin:
        
        fundstransfers = FundsTransfer.objects.all()
        utilitybills = UtilityPayment.objects.all()
        # combine fundstransfers and utilitybills querysets into a single list for pagination
        combinedlogs = list(chain(fundstransfers, utilitybills))
        combinedlogspaginator = Paginator(combinedlogs, 2)

        page = request.GET.get('page')
        try:
            logs = combinedlogspaginator.page(page)
        except PageNotAnInteger:
            # if page is not an integer deliver the first page
            logs = combinedlogspaginator.page(1)
        except EmptyPage:
            # if page is out of range deliver last page of the results
            logs = combinedlogspaginator.page(paginator.num_pages)

    else:
        fundstransfers = FundsTransfer.objects.filter(transferID=userid)
        utilitybills = UtilityPayment.objects.filter(customerName=userid)


    context_dict = {'loggeduser':loggeduser,  'transfers':fundstransfers, 'billpayments':utilitybills, 'logs':logs, 'page':page }

    return render(request, 'bankingapp/accesslogs.html', context = context_dict)

def signup(request):

    context_dict = { }

    return render(request, 'bankingapp/signup.html', context = context_dict)
