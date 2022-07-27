from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.budget), 
    path('add-bucket/', views.add_bucket, name='add-bucket'), 
    path('add-item/', views.add_item, name='add-item'), 
    path('add-account/', views.add_account, name='add-account'), 

    #display 
    path('bucket-list/', views.all_buckets, name='list-buckets'), 
    path('items/<int:bucket_id>/', views.bucket_items, name='bucket_items')
]
