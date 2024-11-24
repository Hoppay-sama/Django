from django.db import models

# Create your models here.
class Phone(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    storage_options = models.ManyToManyField('StorageOption', through='PhoneStorageOption')
    quantity = models.PositiveIntegerField(default=0)
    
class StorageOption(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PhoneStorageOption(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    storage_option = models.ForeignKey(StorageOption, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)