from django.urls import path
from . import views

app_name = 'Cart'

urlpatterns = [
    path('', views.cart_summary, name="Cart_summary"),
    path('add/', views.cart_add, name="Cart_add"),
    path('remove/<int:product_id>', views.cart_remove, name="Cart_remove"),
    path('update/<int:product_id>', views.cart_update, name="Cart_update"),
]