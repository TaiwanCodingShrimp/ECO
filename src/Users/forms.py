from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    ReadOnlyPasswordHashField,
    UserCreationForm,
)

from .models import Leftover, User, Waste


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "title", "phone", "location", "password1", "password2")


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("email", "password")


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("email", "title", "phone", "location")

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save(using=self._db)
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on the user, but replaces the password field with admin's password hash display field."""

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "title",
            "phone",
            "location",
            "is_active",
            "is_staff",
        )

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        return self.initial["password"]


class WasteForm(forms.ModelForm):
    class Meta:
        model = Waste
        fields = ["item", "provider", "label", "sent_to", "status"]


class LeftoverForm(forms.ModelForm):
    class Meta:
        model = Leftover
        fields = ["item", "provider", "label", "portion", "sent_to", "status"]
