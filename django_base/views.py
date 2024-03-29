
import json
from django.shortcuts import render
from coins.models import Coin
from django.contrib.auth.decorators import login_required
from coins.utils import get_five_days_data , get_recent_transactions



@login_required
def index(request):

    context = {
        'graph_data': json.dumps(get_five_days_data()),
        'recents_transactions': get_recent_transactions(),
        'coins': Coin.objects.all(),
        
    }
    return render(request, 'index.html', context=context)