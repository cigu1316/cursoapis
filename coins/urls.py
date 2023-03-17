from django.contrib import admin
from django.urls import path 

from coins.views import coins_list_view ,wallet_list_view ,  portfolio , generate_data , get_five_days_data

urlpatterns = [
    path('list_coins/',coins_list_view, name='coins'),
    path('wallet/',wallet_list_view, name='wallet'),
    path('portfolio/',portfolio, name='portfolio'),
    path('generate-data/',generate_data, name='generate_data'),
    path('get-five-days-data/',get_five_days_data, name='get_five_days_data')
]