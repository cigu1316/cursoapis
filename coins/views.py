from django.shortcuts import render

# Create your views here.
def coins_list_view(request):
    return render(request, 'coins/list_coins.html')

def wallet_list_view(request):
    return render(request, 'wallet.html')

def portfolio_list_view(request):
    return render(request, 'portfolio.html')