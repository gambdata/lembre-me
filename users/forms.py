from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('user_name', 'email', 'password1', 'password2')
        widgets = {
            'user_name': forms.TextInput(attrs={'placeholder': 'username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'name@company.com'})
        }