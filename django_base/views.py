
import json
from django.shortcuts import render
from coins.models import Coin
from django.contrib.auth.decorators import login_required
from coins.views import get_five_days_data

@login_required
def index(request):
    for coin in Coin.objects.all():
        print(coin.get_last_day_price())
        print(coin.get_performance())
    context={ 
             
        'graph_data': json.dumps(get_five_days_data()),
    
    }
    return render(request,'index.html', context=context)