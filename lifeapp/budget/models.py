from datetime import datetime
from decimal import Decimal
#from pydoc import describe
from django.db import models
from django.forms import BooleanField, CharField, DateTimeField, FloatField, Textarea, DecimalField 
from django.utils.timezone import now

# Create your models here. 

class Item(models.Model):  
   
    title = models.CharField(max_length=150, null=False, default='Item') 
    description = models.TextField(null=True, blank=True) 
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=Decimal('0.00')) 
    date_incurred = models.DateField(default=datetime.now) 
    bucket = models.ForeignKey("Bucket", on_delete=models.CASCADE) 
    #is_revenue = models.BooleanField(default=False) 
    

    def __str__(self): 
        return f'{self.title}' 

class Bucket(models.Model):  
    
    title = models.CharField(max_length=150, null=False, default='Bucket') 
    description = models.TextField(null=True, blank=True) 
    is_budget = models.BooleanField(default=True) 
    account = models.ForeignKey("Account", on_delete=models.CASCADE) 
    is_revenue = models.BooleanField(default=False) 
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    def __str__(self): 
        return self.title 

class Account(models.Model): 
    
    title = models.CharField(max_length=150, null=False, default='Checkings Account')
    description = models.TextField(null=True, blank=True) 
    balance = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=Decimal('0.00')) 

    
    def __str__(self): 
        return str(self.title) 
    



