from django.contrib import admin
from admin_settings.models import Country, Language

from coins.models import  Card ,Coin , Transaction

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    
    
@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):  
    list_display = ('name',)
    

   