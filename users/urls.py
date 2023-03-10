from django.urls import path
from users.views import login_view, register ,users_list_view , users_profile_view
from django.contrib.auth.views import LogoutView


urlpatterns = [    
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(template_name = 'users/login.html'), name='logout'),
    path('register/', register, name='register'),
    
    path('list/', users_list_view, name='list'),
    
    path('profile/', users_profile_view , name='profile'),
   
    
]