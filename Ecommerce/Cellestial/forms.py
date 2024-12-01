from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="First Name", max_length=100, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'First Name', 'id':'half'}))
	last_name = forms.CharField(label="Last Name", max_length=100, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Last Name', 'id':'half'}))

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email',  'username', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'input'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = 'Username'
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'input'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = 'Password'
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'input'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = 'Confirm Password'
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'