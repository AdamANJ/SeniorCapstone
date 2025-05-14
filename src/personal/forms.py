from django import forms
from .models import registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = registration
        fields = '__all__'