from datetime import timedelta
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
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='cards')
    card_name = models.CharField(max_length=40)
    card_holder= models.CharField(max_length=60)
    card_number = models.IntegerField(validators=[ 
                                                 MinValueValidator(4300000000000000),
                                                 MaxValueValidator(4399999999999999)
                                                 ])
    bank_name = models.CharField(max_length=80)
    valid_date = models.DateTimeField(max_length=5, default= 'mm/yy')
    color= models.CharField(max_length=7, choices=CHOISES , default='purple')
    balance = models.FloatField(default=15000)
    
    def __str__(self):
        return self.card_name
    
  
class Coin(models.Model):
    
    name = models.CharField(max_length=50)
    code= models.CharField(max_length=10)
    description= models.TextField() 
    image= models.ImageField(upload_to='coins')
    
    
    def __str__(self):
        return self.name
    
    def get_last_day(self):
        return self.transactions.all().order_by('-date').first().date
   
    def get_price_by_date(self , date):
        return self.transactions.filter(date__date=date).aggregate(average = Avg('price'))['average']           
   
    def get_last_five_days_data(self):
        data=[]
        last_day =self.get_last_day()
        for i in range(1,6):
            data.append(round(self.get_price_by_date(last_day),2))
            last_day -= timedelta(days=1)
        return data
         
    def get_average_transactions_by_date(self , date):
        return self.transactions.filter(date__date=date).aggregate(average=Avg('price'))

    def get_last_day_price(self):
        last_day = self.get_last_day()
        return round(self.get_price_by_date(last_day),2)
          
    def get_performance_of_week(self,end_date):
        week_price = 0
        for i in range(0 ,7):
            week_price = self.get_price_by_date(end_date)
            end_date -= timedelta(days=1)
        week_price /= 7
        return (week_price,end_date)
          
    def get_performance(self):
        last_day = self.get_last_day()
        current_week_price , last_day= self.get_performance_of_week(last_day)
        last_week_price , last_day = self.get_performance_of_week(last_day)
        (current_week_price,last_week_price)
        return round(((current_week_price - last_week_price)/(last_week_price)) * 100,2)
   
            
    def get_lasts_transactions(self):
        if self.transactions.count() == 0:
            return []
        return self.transactions.order_by('-date')[:7]
           
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
    
    @classmethod
    def  get_last_day(cls):
        return cls.objects.all().order_by('-date').first().date.date()
    
    def get_total_price(self):
        
        return round(self.price * self.amount, 2)