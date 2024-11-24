from django.contrib import admin
from .models import Phone, StorageOption, PhoneStorageOption
# Register your models here.

class PhoneModels(admin.ModelAdmin):
    list_display = ('name', 'quantity')


admin.site.register(Phone, PhoneModels)
admin.site.register(StorageOption)
admin.site.register(PhoneStorageOption)