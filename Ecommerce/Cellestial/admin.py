from django.contrib import admin
from Cellestial.models import *
# Register your models here.


admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Color)
admin.site.register(Storage)

class CustomerModels(admin.ModelAdmin):
    list_display = ('name', 'email', 'address')
admin.site.register(Customer, CustomerModels)

class ProductModels(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'description')
admin.site.register(Phone, ProductModels)

