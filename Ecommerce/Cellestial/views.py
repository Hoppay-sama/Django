from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from . import models

# Create your views here.
def home(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

def shop(request):  
    products = models.Phone.objects.all()
    return render(request, 'shop.html', {'products':products})
    
def shipping(request):
    template = loader.get_template('shipping.html')
    return HttpResponse(template.render())

def product_page(request, pk):
    template = loader.get_template('product_page.html')
    return HttpResponse(template.render())

def payment(request):
    template = loader.get_template('payment.html')
    return HttpResponse(template.render())

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')