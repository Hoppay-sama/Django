from django.urls import path
from . import views
from .views import logout

app_name = 'users'

urlpatterns = [
    path('register/',views.register, name="Register"),
    path('login/',views.login, name="Login"),
    path('logout/',logout.as_view(), name="Logout"),
]