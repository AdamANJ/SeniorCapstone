from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import Account

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=60, help_text="Enter a valid email")
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50)

	class Meta:
		model = Account
		fields = ("email", "first_name", "last_name")