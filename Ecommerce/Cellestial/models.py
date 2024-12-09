from django.db import models
import datetime

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100)

    verbose_name_plural = 'Categories'
    
    def __str__ (self):
        return self.name
    
    
class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__ (self):
        return self.name
    
class Storage(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=2500)

    def __str__ (self):
        return self.name
    


class Phone(models.Model):
    image = models.ImageField(upload_to='uploads/products/')
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=7999)
    description = models.CharField(max_length=256, default='', blank=True, null=True)
    color = models.ManyToManyField(Color)
    storage = models.ManyToManyField(Storage)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.is_sale:
            self.category = Category.objects.get(name='Discounts')
        super().save(*args, **kwargs)


class Order(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    address = models.CharField(max_length=200, blank=True, null=True)
    date_ordered = models.DateTimeField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer.name}"
