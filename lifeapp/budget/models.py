from datetime import datetime
from pydoc import describe
from django.db import models
from django.forms import BooleanField, CharField, DateTimeField, FloatField, Textarea, DecimalField 
from django.utils.timezone import now

# Create your models here. 

class Item(models.Model): 
    title = CharField(max_length=150) 
    description = Textarea() 
    amount = DecimalField(max_digits=10, decimal_places=2) 
    date_incurred = models.DateTimeField(default=datetime.now) 
    bucket = models.ForeignKey("Bucket", on_delete=models.CASCADE) 
    is_revenue = BooleanField() 
    

    def __str__(self): 
        return f'{self.title}' 

class Bucket(models.Model): 
    title = CharField(max_length=150) 
    description = Textarea() 
    is_budget = BooleanField() 
    account = models.ForeignKey("Account", on_delete=models.CASCADE) 

    def __Str__(self): 
        return f'{self.title}' 

class Account(models.Model): 
    title = CharField(max_length=150)
    description = Textarea() 
    balance = DecimalField(max_digits=10, decimal_places=2) 
    



