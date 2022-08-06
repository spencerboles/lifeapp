from django.shortcuts import render, redirect 
from .forms import BucketForm, ItemForm, AccountForm 
from .models import Bucket, Item 
import plotly.express as px 
from django.db.models import Sum

# Create your views here.
def budget(request): 
    return render(request, 'base.html') 

def add_bucket(request): 
    if request.method == 'POST':
        form = BucketForm(request.POST)  
        if form.is_valid():
            form.save() 
            return redirect("/budget")
    else: 
        form = BucketForm()  
        return render(request, 'input/form.html', {"form":form, "title": "Bucket"}) 

def add_item(request): 
    if request.method == 'POST': 
        form = ItemForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('/budget/add-item') 
    else: 
        form = ItemForm() 
        return render(request, 'input/form.html', {"form": form, "title": "Item"})

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
    bucket_list = Bucket.objects.all() 
    return render(request, 'display/bucket_list.html', {'buckets':bucket_list}) 

def bucket_items(request, bucket_id): 
    items = Item.objects.filter(bucket__id=bucket_id) 
    graph_items = Item.objects.values('date_incurred').filter(bucket__id=bucket_id).annotate(date_sum=Sum('amount')) 
    
    fig = px.line( 
        x=[item['date_incurred'] for item in graph_items], 
        #x=[num for num in range(len(graph_items))], 
        y=[item['date_sum'] for item in graph_items]
    ) 

    chart = fig.to_html() 

    return render(request, 'display/items.html', {'items': items, 'chart':chart})

def bucket_items_month(request, bucket_id, year, month): 
    items = Item.objects.filter(bucket__id=bucket_id, date_incurred__year=year, date_incurred__month=month) 
    graph_items = Item.objects.values('date_incurred').filter(bucket__id=bucket_id, date_incurred__year=year, date_incurred__month=month).annotate(date_sum=Sum('amount')) 
    
    fig = px.line( 
        x=[item['date_incurred'] for item in graph_items], 
        #x=[num for num in range(len(graph_items))], 
        y=[item['date_sum'] for item in graph_items]
    ) 

    chart = fig.to_html() 



    return render(request, 'display/items.html', {'items': items, 'chart':chart})