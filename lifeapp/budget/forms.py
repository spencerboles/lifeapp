from django.forms import CheckboxInput, DateTimeInput, DecimalField, ModelForm, NumberInput  
from django import forms
from .models import Bucket, Item, Account 

class BucketForm(ModelForm): 
    class Meta: 
        model = Bucket 
        fields = '__all__'  

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-2 mt-2'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-2 mt-2'}), 
            'is_budget': forms.CheckboxInput(), 
            'account': forms.Select(attrs={'class': 'form-control mb-2 mt-2'})  
        }


class ItemForm(ModelForm): 
    class Meta: 
        model = Item 
        fields='__all__' 

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-2 mt-2'}), 
            'description': forms.Textarea(attrs={'class': 'form-control mb-2 mt-2'}), 
            'amount': forms.NumberInput(attrs={'class': 'form-control mb-2 mt-2'}), 
            'date_incurred': forms.DateTimeInput(attrs={'class': 'form-control mb-2 mt-2'}), 
            'bucket': forms.Select(attrs={'class': 'form-control mb-2 mt-2'}), 
            'is_revenue': forms.CheckboxInput()
        } 

class AccountForm(ModelForm): 
    class Meta: 
        model = Account 
        fields = '__all__' 

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-2 mt-2'}),
             'description': forms.Textarea(attrs={'class': 'form-control mb-2 mt-2'}), 
             'balance': forms.NumberInput(attrs={'class': 'form-control mb-2 mt-2'})
        }