from django.shortcuts import render,redirect
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
def portfolio(request):
    return render(request, 'coins/portfolio.html')

def generate_data(request):
    generate_transactions()
    return HttpResponse('Data generated')


@login_required 
def wallet_list_view(request):
    if request.method == 'GET':
        context={
            
            'cards': Card.objects.filter(user = request.user)
            
        }
        return render(request, 'coins/wallet.html', context=context)

@login_required
def card_delete(request,pk):
    card = Card.objects.get(pk=pk)
    card.delete()
    return redirect('wallet')