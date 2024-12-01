from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as logout_user
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import loader
from django.urls import reverse
from django import forms
from . import models, forms

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'welcome back' + username)
            return HttpResponseRedirect(reverse('Cellestial:Home'))
        else:
            messages.error(request, 'Username or password is incorrect')
    else:
        return render(request, 'login.html', {})

def logout(request):
    logout_user(request)
    messages.success(request, 'User logged out')
    return redirect('Cellestial:Home')

def register(request):
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('Cellestial:Home')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        return render(request, 'register.html', {'form': form})

# MAIN
def home(request):
    return render(request, 'homepage.html', {})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def shop(request):  
    try:
        products = models.Phone.objects.all()
        return render(request, 'shop.html', {'products': products})
    except Exception as e:
        messages.error(request, f'An error occurred while fetching products: {e}')
        return render(request, 'shop.html', {})

# Product Detail    
def product(request, pk):
    product = models.Phone.objects.get(id=pk)
    return render(request, 'details.html', {'product': product})

# Checkouts
def shipping(request):
    return render(request, 'shipping.html')

def payment(request):
    return render(request, 'payment.html')

def ToC(request):
    return render(request, 'terms_and_con.html')