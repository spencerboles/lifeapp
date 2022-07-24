from pydoc import describe
from django.db import models
from django.forms import BooleanField, CharField, DateTimeField, FloatField 
import datetime

# Create your models here. 

class Item(models.Model): 
    title = CharField(max_length=150) 
    description = TextField(max_length=300) 
    amount = FloatField()
    date_incurred = DateTimeField(default=datetime.now()) 
    bucket = models.ForeignKey("Bucket", on_delete=models.CASCADE) 
    isRevenue = BooleanField() 
    

    def __str__(self): 
        return f'{self.title}' 

class Bucket(models.Model): 
    title = CharField(max_length=150) 
    description = TextField(max_length=300) 
    is_budget = BooleanField()


