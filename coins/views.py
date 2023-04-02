from django.shortcuts import render,redirect
from coins.models import Card
from django.http import HttpResponse 
from coins.utils import generate_transactions
from coins.models import Coin 
from django.contrib.auth.decorators import login_required 
from coins.models import Transaction
from datetime import datetime
import random


from coins.forms import CardForm


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
def wallet_view(request):
    if request.method == 'GET':
        context = {
            'cards': Card.objects.filter(user=request.user)
        }
        return render(request,'coins/wallet.html', context=context)
    
    elif request.method == 'POST':

        data = request.POST.copy()
        data['valid_date'] = datetime.strptime(request.POST['valid_date'],'%m/%y').date()
        

        form = CardForm(data)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = request.user
            card.balance = random.randint(5000, 30000)
            card.save()
            return redirect('wallet')
        else:
            context = {
                'cards': Card.objects.filter(user=request.user),
                'errors': form.errors,
            }
            return render(request,'coins/wallet.html', context=context)


@login_required
def card_delete(request,pk):
    card = Card.objects.get(pk=pk)
    card.delete()
    return redirect('wallet')
