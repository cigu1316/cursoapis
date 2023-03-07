from django.contrib import admin
from django.urls import path 

from coins.views import coins_list_view ,wallet_list_view ,portfolio_list_view

urlpatterns = [
    path('list_coins/',coins_list_view, name='coins'),
    path('wallet/',wallet_list_view, name='wallet'),
    path('portfolio/',portfolio_list_view, name='portfolio')
]