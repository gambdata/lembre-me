from django.contrib.auth.forms import UserCreationForm
from .models import NewUser

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ('user_name', 'email', 'password1', 'password2')
