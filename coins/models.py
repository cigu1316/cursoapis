from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Card(models.Model):
    
    CHOISES= [
        ('purple', 'purple'),
        ('blue', 'blue'),
        ('green', 'green'),
        ('orange', 'orange'),
            
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_name = models.CharField(max_length=40)
    card_holder= models.CharField(max_length=60)
    card_number = models.IntegerField(validators=[ 
                                                 MinValueValidator(4300000000000000),
                                                 MaxValueValidator(4399999999999999)
                                                 ])
    bank_name = models.CharField(max_length=80)
    valid_date = models.CharField(max_length=40)
    color= models.CharField(max_length=7, choices=CHOISES , default='purple')
    
    def __str__(self):
        return self.card_name