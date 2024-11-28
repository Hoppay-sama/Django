from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__ (self):
        return self.name
    
class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__ (self):
        return self.name
    
class Storage(models.Model):
    name = models.CharField(max_length=255)

    def __str__ (self):
        return self.name
    

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=100)


class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=256, default='', blank=True, null=True)
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='uploads/products/')

    def save(self, *args, **kwargs):
        if self.is_sale:
            self.category = Category.objects.get(name='Discounts')
        super().save(*args, **kwargs)


class Order(models.Model):
    product = models.ForeignKey(Phone, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    address = models.CharField(max_length=200, blank=True, null=True)
    date_ordered = models.DateTimeField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
