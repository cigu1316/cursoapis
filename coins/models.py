from django.db import models
from django.contrib.auth.models import User

class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_name = models.CharField(max_length=40)
    card_holder= models.CharField(max_length=60)
    #card_number = models.CharField()
    bank_name = models.CharField(max_length=80)
    valid_date = models.CharField(max_length=40)
   