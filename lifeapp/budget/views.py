from django.shortcuts import render, redirect 
from .forms import BucketForm, ItemForm, AccountForm 
from .models import Bucket, Item, Account 
import plotly.express as px 
from django.db.models import Sum 
from datetime import datetime

# Create your views here.
def budget(request): 
    return render(request, 'base.html') 

def add_bucket(request): 
    if request.method == 'POST':
        form = BucketForm(request.POST)  
        if form.is_valid():
            form.save() 
            return redirect("/budget/bucket-list")
    else: 
        form = BucketForm()  
        return render(request, 'input/form.html', {"form":form, "title": "Bucket"}) 

def add_item(request): 
    if request.method == 'POST': 
        form = ItemForm(request.POST) 
        if form.is_valid(): 
            
            amount = form.cleaned_data['amount']  
            bank_account = Bucket.objects.get(pk=int(form.cleaned_data['bucket'].id)).account 

            bank_account.balance = bank_account.balance - amount  

           
            form.save()  
            bank_account.save() 
             
            return render(request, 'input/form.html', {"form": form, "title": "Expense Item", 'success_message': 'Transaction Posted.'}) 
            #return redirect('/budget/add-item') 
    else: 
        form = ItemForm() 
        return render(request, 'input/form.html', {"form": form, "title": "Expense Item"})

def add_revenue_item(request): 
    if request.method == 'POST': 
        form = ItemForm(request.POST) 
        if form.is_valid(): 
            
            amount = form.cleaned_data['amount']  
            bank_account = Bucket.objects.get(pk=int(form.cleaned_data['bucket'].id)).account 

            bank_account.balance = bank_account.balance + amount  
            form.is_revenue = True
           
            form.save()  
            bank_account.save() 
             
            return render(request, 'input/form.html', {"form": form, "title": " Revenue Item", 'success_message': 'Transaction Posted.'}) 
            #return redirect('/budget/add-item') 
    else: 
        form = ItemForm() 
        return render(request, 'input/form.html', {"form": form, "title": "Revenue Item"})

def add_account(request): 
    if request.method == 'POST': 
        form = AccountForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('/budget/add-account') 
    else: 
        form = AccountForm() 
        return render(request, 'input/form.html', {"form": form, "title": "Account"}) 

def all_buckets(request): 
    #date = {'year': datetime.now().year,'month': datetime.now().month} 
    year = datetime.now().year 
    month = datetime.now().month
    
    bucket_list = Bucket.objects.all()  
    bucket_sum = Item.objects.select_related('bucket').values('bucket').annotate(bucket_sum=Sum('amount'))



    return render(request, 'display/bucket_list.html', {'buckets':bucket_list, 'year':year, 'month':month, 'bucket_sum': bucket_sum}) 

def bucket_items(request, bucket_id): 
    items = Item.objects.filter(bucket__id=bucket_id) 
    graph_items = Item.objects.values('date_incurred').filter(bucket__id=bucket_id).annotate(date_sum=Sum('amount')) 
    bucket = Item.objects.filter(id=bucket_id)
    if len(graph_items) > 0:
        fig = px.line( 
            x=[item['date_incurred'] for item in graph_items], 
            #x=[num for num in range(len(graph_items))], 
            y=[item['date_sum'] for item in graph_items], 
            labels=dict(x='Date', y='Amount ($)'), 
            markers=True
        ) 
        fig.update_xaxes(type='category') 
        fig.update_traces(marker=dict(size=12)) 
        chart = fig.to_html()  
    else: 
        chart = 0

    return render(request, 'display/items.html', {'items': items, 'chart':chart, 'bucket':bucket})

def bucket_items_month(request, bucket_id, year, month): 
    items = Item.objects.filter(bucket__id=bucket_id, date_incurred__year=year, date_incurred__month=month) 
    graph_items = Item.objects.values('date_incurred').filter(bucket__id=bucket_id, date_incurred__year=year, date_incurred__month=month).annotate(date_sum=Sum('amount')) 
    bucket = Bucket.objects.filter(id=bucket_id).first 
    #print(bucket) 

    if len(graph_items) > 0:
        fig = px.line( 
            x=[item['date_incurred'] for item in graph_items], 
            #x=[num for num in range(len(graph_items))], 
            y=[item['date_sum'] for item in graph_items], 
            labels=dict(x='Date', y='Amount ($)'), 
            markers=True
        ) 
        fig.update_xaxes(type='category') 
        fig.update_traces(marker=dict(size=12)) 

        chart = fig.to_html()  
    else: 
        chart = 0



    return render(request, 'display/items.html', {'items': items, 'chart':chart, 'bucket':bucket})

def account_items(request, account_id):  
    account = Account.objects.filter(id=account_id).first()
    items = Item.objects.filter(bucket__account=account_id)  
    total_spent = items.filter(date_incurred__year=2022, date_incurred__month=8, is_revenue=False).annotate(total_sum=Sum('amount')).aggregate(Sum('total_sum'))
    if total_spent['total_sum__sum'] == None:
        total_spent = 0 
    else: 
        total_spent = float(total_spent['total_sum__sum'])
    
    total_revenue = items.filter(date_incurred__year=2022, date_incurred__month=8, is_revenue=True).annotate(total_sum=Sum('amount')).aggregate(Sum('total_sum'))

    if total_revenue['total_sum__sum'] == None:
        total_revenue = 0 
    else: 
        total_revenue = float(total_revenue['total_sum__sum'])

    graph_items = items.filter(date_incurred__year=2022, date_incurred__month=8).values('date_incurred').annotate(date_sum=Sum('amount'))
    
    if len(graph_items) > 0:
        fig = px.line( 
            x=[item['date_incurred'] for item in graph_items], 
            #x=[num for num in range(len(graph_items))], 
            y=[item['date_sum'] for item in graph_items], 
            labels=dict(x='Date', y='Amount ($)'), 
            markers=True
        ) 
        fig.update_xaxes(type='category') 
        fig.update_traces(marker=dict(size=12)) 
        chart = fig.to_html()  
    else: 
        chart = 0
    
    return render(request, 'display/account.html', {'account': account, 'items':items, 'total_spent':total_spent, 'chart':chart})

def budget_dashboard(request):
    return render(request, 'display/budget_dashboard.html')
