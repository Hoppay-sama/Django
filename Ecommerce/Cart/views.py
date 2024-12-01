from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def cart_summary(request):
    return render(request, 'cart_summary.html', {})

def cart_add(request):
    pass

def cart_remove(request):
    pass

def cart_update(request):
    pass    