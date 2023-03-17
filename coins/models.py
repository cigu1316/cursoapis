from datetime   import timedelta

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg
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
    
  
class Coin(models.Model):
    
    name = models.CharField(max_length=50)
    code= models.CharField(max_length=10)
    description= models.TextField() 
    image= models.ImageField(upload_to='coins')
    
    
    def __str__(self):
        return self.name
    
    def get_last_date(self):
        return self.transactions.all().order_by('-date').first().date
    
    def get_average_transactions_by_date(self , date):
        return self.tarnsactions.filter(date__date=date).aggregate(average = Avg('price'))
        
    def get_last_five_days_data(self):
        last_day =self.get_last_day()
        for i in range(1,6):
            last_day -= timedelta(days=1)
        
      
        
class Transaction(models.Model):
    
    CHOISES= [
        ('buy', 'buy'),
        ('sell', 'sell'),
    ]
    
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE,related_name='transactions')
    price = models.FloatField()
    amount = models.FloatField()
    date = models.DateTimeField()
    transaction_type = models.CharField(max_length=4, choices=CHOISES)
     
    def __str__(self):
        return self.coin.name + ' ' + self.transaction_type 
  