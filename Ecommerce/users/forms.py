from django import forms
from . import models
from .models import Register
from django.utils.safestring import mark_safe
from django.contrib.auth.hashers import make_password, check_password
from .auth_backends import CustomAuthBackend

class register(forms.ModelForm):
    confirm_password = forms.CharField(max_length=100, label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class':'input'}))

    class Meta:
        model = models.Register
        fields = ["first_name","last_name","phone_number","email","username","password", 'confirm_password', 'terms_and_conditions']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Jhon', 'class':'input', 'id':'half'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Doe', 'class':'input', 'id':'half'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '09123456789', 'class':'input', 'id':'half'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Example@example.com', 'class':'input', 'id':'half'}),
            'username': forms.TextInput(attrs={'placeholder': 'JohnDoe', 'class':'input'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class':'input'}),
            'confirm_password': forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class':'input'}),
            'terms_and_conditions': forms.CheckboxInput(attrs={'class':'terms-and-conditions'}),
        }
        labels = {
            'terms_and_conditions': mark_safe('I agree to the <a id="ToC" href="#" target="_blank">Terms and Conditions</a>'),
        }

    def check_password(self, password):
        return check_password(password, self.password)
    
    def clean_terms_and_conditions(self):
        terms_and_conditions = self.cleaned_data['terms_and_conditions']
        if not terms_and_conditions:
            raise forms.ValidationError("You must agree to the terms and conditions to register.")
        return terms_and_conditions

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    password = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput)
    backend = CustomAuthBackend()


    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Enter Username', 'class':'input-text'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class':'input-text'})

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = self.backend.authenticate(request=self.request, username=username, password=password)
        if user is None:
            self.add_error('username', 'Invalid username or password')
            self.add_error('password', 'Invalid username or password')
        return cleaned_data

    def authenticate(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = self.backend.authenticate(request=self.request, username=username, password=password)
        if user is not None:
            self.request.session['user_id'] = user.id
            return True
        return False