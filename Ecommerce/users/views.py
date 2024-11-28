from django.shortcuts import render, redirect
from . import forms
from .models import Register    
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form is not None:
#             if form.is_valid():
#                 form.save()
#                 return redirect('Cellestial:Home')
#         else:
#             pass
#     else:
#         form = UserCreationForm()
#     return render(request,'register.html', {'form':form})

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = forms.register(request.POST)
        if form is not None:
            if form.is_valid():
                form.save()
                return redirect('Cellestial:Home')
        else:
            pass
    else:
        form = forms.register()
    return render(request,'register.html', {'form':form})


def login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST, request=request)
        if form.is_valid():
            if form.authenticate():
                return redirect('Cellestial:Home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = forms.LoginForm()
    return render(request, 'login.html', {'form': form})

class logout(LogoutView):
    template = 'logout.html'

    def get_redirect_url(self):
        return reverse_lazy('Cellestial:Home')