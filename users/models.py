from django.contrib.auth.models import User
from django.db import models

from admin_settings.models import Country, Language

class UserProfile(models.Model):

    CHOICE = (
        ('full-time', 'full-time'),
        ('part-time', 'part-time'),
        ('freelance', 'freelance'),
        ('other', 'other')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE ,related_name='profile')
    phone_number = models.CharField(max_length=30 , blank=True , null=True )
    profile_image = models.ImageField(upload_to='profile_image', blank=True , null=True,default='profile_image/default.jpg')
    cover_image = models.ImageField(upload_to='cover_image',blank=True , null=True,default='cover_image/default.jpg')
    occupation = models.CharField(max_length=100, blank=True , null=True)
    description = models.TextField( blank=True , null=True)
    availability  = models.CharField(max_length=100, choices=CHOICE , blank=True , null=True)
    birth_date = models.DateField( blank=True , null=True)
    years_of_experience = models.PositiveIntegerField( blank=True , null=True)
    address = models.CharField(max_length=150, blank=True , null=True)
    company_name = models.CharField(max_length=100, blank=True , null=True)
    facebook = models.URLField( blank=True , null=True)   
    country = models.ForeignKey('admin_settings.Country', on_delete=models.RESTRICT,blank=True , null=True)
    language = models.ForeignKey('admin_settings.Language', on_delete=models.RESTRICT,blank=True , null=True)
    
        
   
    def __str__(self):
        return self.user.username