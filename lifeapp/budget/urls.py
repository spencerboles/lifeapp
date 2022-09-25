from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.budget_dashboard), 
    path('add-bucket/', views.add_bucket, name='add-bucket'), 
    path('add-expense-item/', views.add_item, name='add-item'),
    path('add-revenue-item/', views.add_revenue_item, name='add-revenue-item'), 
    path('add-account/', views.add_account, name='add-account'), 
    

    #display 
    path('bucket-list/', views.all_buckets, name='list-buckets'), 
    path('items/<int:bucket_id>/', views.bucket_items, name='bucket-items'),
    path('items/<int:bucket_id>/<int:year>/<int:month>', views.bucket_items_month, name='bucket-items-year'),  
<<<<<<< HEAD
    path('account/<int:account_id>', views.account_items, name='account-items'), 
=======
    path('account/<int:account_id>', views.account_items, name='account-items') 
>>>>>>> fc49898329785335c77c7b3b65da7f05e511916e
    
]
