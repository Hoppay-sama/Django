from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .cart import *
from Cellestial.models import *
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_product
    return render(request, 'cart_summary.html', {'cart_products': cart_products})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Phone, id=product_id)
        cart.add(product=product)
        return JsonResponse({'status': product.name + ' was added to your cart'})

def cart_remove(request):
    pass

def cart_update(request):
    pass    