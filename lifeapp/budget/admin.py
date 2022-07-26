from django.contrib import admin
from .models import Item, Bucket, Account
# Register your models here. 

'''class AccountAdmin(admin.ModelAdmin):  
    model = Account
    list_display = ['title', 'description', 'balance'] 


class BucketAdmin(admin.ModelAdmin):  
    model = Bucket
    list_display = ['title', 'description', 'is_budget'] 

    def get_name(self, obj): 
        return obj.account.title '''

admin.site.register(Account)
admin.site.register(Bucket) 
admin.site.register(Item)
