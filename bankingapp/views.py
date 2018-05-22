from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {}

    return render(request, 'bankingapp/index.html', context=context_dict)

def Apphome(request):
     context_dict = {}

     return render(request, 'bankingapp/home.html', context=context_dict)

def transactions(request):
    context_dict = {}

    return render(request, 'bankingapp/transactions.html', context=context_dict)

def monthlystatements(request):
    context_dict = {}

    return render(request, 'bankingapp/monthlystatements.html', context=context_dict)


def fundstransfer(request):

    context_dict = {}

    return render(request, 'bankingapp/fundstransfer.html', context=context_dict)

def payutilities(request):

    context_dict = {}

    return render(request, 'bankingapp/payutilities.html', context = context_dict)

def updateprofile(request):

    context_dict = {}

    return render(request, 'bankingapp/updateprofile.html', context = context_dict)

def accesslogs(request):

    context_dict = { }

    return render(request, 'bankingapp/accesslogs.html', context = context_dict)
