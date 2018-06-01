from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from bankingapp.models import UtilityPayment, FundsTransfer, UserProfile, UserBankAccount
from django.contrib.auth import authenticate, login
from bankingapp.forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

class HomeView(RedirectView):
     template_name = 'bankingapp/home.html'
     url = reverse_lazy('Apphome')

def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleanedform = form.cleaned_data
            user = authenticate(username=cleanedform['username'], password=cleanedform['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    context_dict = { 'form': form }

    return render(request, 'bankingapp/index.html', context=context_dict)


@login_required
def Apphome(request):


     return render(request, 'bankingapp/home.html', {'section': 'Apphome'})

@login_required
def fundstransactions(request):
    fundstransfers = FundsTransfer.objects.all()
    fundstransferpaginator = Paginator(fundstransfers, 10) # List up to 10 fundstransfer transactions
    page = request.GET.get('page')

    try:
        transfers = fundstransferpaginator.page(page)
    except PageNotAnInteger:
        transfers = fundstransferpaginator.page(1)
    except EmptyPage:
        transfers = fundstransferpaginator.page(paginator.num_pages)

    context_dict = {'transfers':transfers, 'page':page }

    return render(request, 'bankingapp/fundstransactions.html', context= context_dict)

@login_required
def utilitybillstransactions(request):
    utilitybills = UtilityPayment.objects.all()
    billspaginator = Paginator(utilitybills, 3) # List 3 utility bills per page
    page = request.GET.get('page')
    try:
        bills = billspaginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        bills = billspaginator.page(1)
    except EmptyPage:
        # if page is out of range deliver last page of the results
        bills = billspaginator.page(paginator.num_pages)
    context_dict = {'bills':bills, 'page':page}

    return render(request, 'bankingapp/utilitybillstransactions.html', context=context_dict)

@login_required
def monthlystatements(request):
    context_dict = {}

    return render(request, 'bankingapp/monthlystatements.html', context=context_dict)

@login_required
def fundstransfer(request):

    context_dict = {}

    return render(request, 'bankingapp/fundstransfer.html', context=context_dict)


@login_required
def payutilities(request):

    context_dict = {}

    return render(request, 'bankingapp/payutilities.html', context = context_dict)

@login_required
def updateprofile(request):

    context_dict = {}

    return render(request, 'bankingapp/updateprofile.html', context = context_dict)

@login_required
def accesslogs(request):

    context_dict = { }

    return render(request, 'bankingapp/accesslogs.html', context = context_dict)

def signup(request):

    context_dict = { }

    return render(request, 'bankingapp/signup.html', context = context_dict)
