from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "title", "phone", "location", "password1", "password2")


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("email", "password")
