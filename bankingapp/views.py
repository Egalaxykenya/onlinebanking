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
