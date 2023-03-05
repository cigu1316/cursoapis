from django.urls import path
from .views import login_view , register
from django.contrib.auth.views import LogoutView

urlpatterns = [    
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(template_name = 'users/login.html'), name='logout'),
    path('register/', register, name='register'),
]