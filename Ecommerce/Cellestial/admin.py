from django.contrib import admin
from Cellestial.models import *
from users.models import Register
# Register your models here.


admin.site.register(Category)
admin.site.register(Order)

class RegisterModels(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'phone_number', 'email')
admin.site.register(Register, RegisterModels)

class CustomerModels(admin.ModelAdmin):
    list_display = ('name', 'email', 'address')
admin.site.register(Customer, CustomerModels)

class ProductModels(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'description')
admin.site.register(Phone, ProductModels)

