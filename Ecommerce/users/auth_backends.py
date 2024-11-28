from django.contrib.auth.hashers import check_password
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from .models import Register

class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = Register.objects.get(username=username)
            if user.check_password(password):
                return user
        except Register.DoesNotExist:
            pass

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
        
def get_user(self, username):
    try:
        return Register.objects.get(username=username)
    except Register.DoesNotExist:
        return None
    