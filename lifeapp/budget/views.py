from django.shortcuts import render, redirect 
from .forms import BucketForm, ItemForm, AccountForm 
from .models import Bucket, Item

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
    return render(request, 'display/items.html', {'items': items})