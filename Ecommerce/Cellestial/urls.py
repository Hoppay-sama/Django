from django.urls import path
from . import views

app_name = 'Cellestial'

urlpatterns = [
    path('login/', views.login, name="Login"),
    path('logout/', views.logout, name="Logout"),
    path('Register/', views.register, name="Register"),

    path('',views.home,name="Home"),
    path('About/', views.about, name="About"),
    path('Contact/', views.contact, name="Contact"),
    path('Terms-and-Conditions/', views.ToC, name="ToC"),
    path('Shop/', views.shop, name="Shop"),
    path('Product/<int:pk>/', views.product, name="Product"),
    
    path('Shipping/', views.shipping, name="Shipping"),
    path('Payment/', views.payment, name="Payment"),
]       