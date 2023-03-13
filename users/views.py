from django.shortcuts import render ,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from users.forms import RegisterForm , UserProfileForm

from django.db.models.signals import post_save
from django.dispatch  import receiver
from django.contrib.auth.models import User
from users.models import UserProfile
from admin_settings.models import Language, Country
import requests
from news.utils import get_random_news

def login_view(request):
    
    
    if request.method == 'GET':
       return render(request, 'users/login.html') 
    
    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        else:
                context = {
                    'errors': form.errors,
                    }
        return render(request, 'users/login.html', context)

def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html') 
    elif request.method == 'POST':
        form =RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context = {
                'errors': form.errors,
                }
            return render(request, 'users/register.html', context)
    

def users_list_view(request):
    return render(request, 'users/users_list.html')

  
    
def user_profile_view(request):
    if request.method == 'GET':
        main_news, other_news , other_news1 ,other_news2 = get_random_news()
        context = {
            'languages': Language.objects.all(),
            'countries': Country.objects.all(),
            'main_news': main_news,
            'other_news': other_news,
            'other_news1': other_news1,
            'other_news2': other_news2,
        }
        return render(request, 'users/user_profile.html', context=context)
    elif request.method == 'POST':
    
        data = request.POST.copy()
    
        if request.POST.get('country')and Country.objects.filter(name = request.POST.get('country')).exists():
            data['country'] = Country.id
            
        if request.POST.get('language')and Language.objects.filter(name = request.POST.get('language')).exists():
            languaje = Language.objects.get(name = request.POST.get('language'))    
            data['language'] = Language.id
            
        form = UserProfileForm(data,request.FILES,instance=request.user.profile)
        
        if form.is_valid():
            form.save()
            print('errors')
            return redirect('profile')
    else:
        context ={
            'errors': form.errors,
            'languages' : Language.objects.all(),
            'countries' : Country.objects.all(),          
        }
        return render (request , 'users/user_profile.html', context=context)

     
  

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
