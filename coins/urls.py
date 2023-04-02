from django.contrib import admin
from django.urls import path 

from coins.views import coins_list_view ,wallet_view ,  portfolio , generate_data , card_delete

urlpatterns = [
    path('list_coins/',coins_list_view, name='coins'),
    path('wallet/',wallet_view, name='wallet'),
    path('portfolio/',portfolio, name='portfolio'),
    path('generate-data/',generate_data, name='generate_data'),
    path('card-delete/<int:pk>/',card_delete, name='card_delete'),
  
]