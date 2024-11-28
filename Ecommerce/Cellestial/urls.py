from django.urls import path
from . import views

app_name = 'Cellestial'

urlpatterns = [
    path('',views.home,name="Home"),
    path('Shop/', views.shop, name="Shop"),
    path('Shipping/', views.shipping, name="Shipping"),
    path('Product_Page/<int:pk>', views.product_page, name="Product_Page"),
    path('Payment/', views.payment, name="Payment"),
    path('About/', views.about, name="About"),
    path('Contact/', views.contact, name="Contact"),
]       