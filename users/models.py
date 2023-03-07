from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    
    CHOISES = (
        ('full_time', 'full Time'),
        ('part_time', 'part Time'),
        ('freelance', 'freelance'),
        ('other', 'other'),
        
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE ,related_name='profile')
    phone_number = models.CharField(max_length=30, blank=True , null=True)
    image = models.ImageField(upload_to='profile_image', blank=True , null=True)
    cover_image = models.ImageField(upload_to='cover_image', blank=True , null=True)
    occupation = models.CharField(max_length=100, blank=True , null=True)
    description = models.TextField(blank=True , null=True)
    availability = models.CharField(max_length=100, blank=True , null=True)
    birth_date = models.DateField(blank=True , null=True)
    years_of_experience = models.PositiveIntegerField(blank=True , null=True)
    company_name = models.CharField(max_length=100, blank=True , null=True)
    adrress = models.CharField(max_length=150, blank=True , null=True)
    
    #languaje = models.CharField(max_length=100, blank=True , null=True)
    #country = models.CharField(max_length=100, blank=True , null=True)
    

    def __str__(self):
        return self.user.username