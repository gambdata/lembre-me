from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Usuario

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username','class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'name@example.com','class': 'form-control'})
        }
    password1 = forms.CharField(label='Senha',widget=forms.PasswordInput(attrs={'placeholder': 'Senha','class': 'form-control'}))
    password2 = forms.CharField(label='Confirme a senha',widget=forms.PasswordInput(attrs={'placeholder': 'Repetir senha','class': 'form-control'}))

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'placeholder': 'name@example.com','class': 'form-control'}))
    password = forms.CharField(label='Sua senha',widget=forms.PasswordInput(attrs={'placeholder': 'Senha','class': 'form-control'}))
