from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import FormView
from django.contrib.auth import login

from .forms import CustomUserCreationForm

class Login(LoginView):
    template_name = 'users/accounts/login.html'

class Logout(LogoutView):
    next_page = '/'

class RegisterUser(FormView):
    template_name = 'users/accounts/register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
