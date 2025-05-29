from django import forms
from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm
from .models import Usuario

class CustomUserCreationForm(AdminUserCreationForm):

    class Meta:
        model = Usuario
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'name@company.com'})
        }

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'name@company.com'})
        }
