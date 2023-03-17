from django.shortcuts import render
from coins.models import Card
from django.http import HttpResponse
from coins.utils import generate_transactions
from coins.models import Coin
from django.contrib.auth.decorators import login_required 

@login_required  # @login_required 
def coins_list_view(request):
    return render(request, 'coins/list_coins.html')
# @login_required 

@login_required 
def wallet_list_view(request):
    return render(request, 'coins/wallet.html')


@login_required 
def portfolio(request):
    return render(request, 'coins/portfolio.html')

def generate_data(request):
    print(generate_transactions())
    return HttpResponse('Data generated')

def get_five_days_data(request):
    for coin in Coin.objects.all():
        coin.get_last_five_days_data()
    return HttpResponse('Data generated')


