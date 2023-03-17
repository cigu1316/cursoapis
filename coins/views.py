from django.shortcuts import render
from coins.models import Card
from django.http import HttpResponse
from coins.utils import generate_transactions
from coins.models import Coin
from django.contrib.auth.decorators import login_required 
from coins.models import Transaction
from datetime import timedelta



@login_required  
def coins_list_view(request):
    return render(request, 'coins/list_coins.html')


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
    context={
        'data':[]
    }
    date_array=[Transaction.get_last_day()]
    for i in range(1 ,5):
        date_array.append(date_array[0] - timedelta(days=i))
    dates = date_array
    
    count=0
    for coin in Coin.objects.all():
        context['data'][count]['name']=coin.name
        context['data'][count]['data']=coin.get_last_five_days_data()
     
    return HttpResponse('Data generated')


