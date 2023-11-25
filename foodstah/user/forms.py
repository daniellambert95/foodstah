from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
import re

User = get_user_model()

class UserSignupForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_username(self):
        username = self.cleaned_data["username"].lower()

        if not re.match(r"^[A-Za-z0-9_]+$", username):
            raise forms.ValidationError(
                "Sorry, your username must only contain letters, numbers and underscores."
            )
        elif (
            User.objects.exclude(pk=self.instance.pk).filter(username=username).exists()
        ):
            raise forms.ValidationError(f"Username {username} is already in use.")
        else:
            return username

    def clean_email(self):
       email = self.cleaned_data.get('email')

       if User.objects.filter(email=email).exists():
           raise forms.ValidationError(f"The email {email} is already in use.")

       return email


class UserLogInForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username').lower()
        password = self.cleaned_data.get('password')

        if username and password:
            self.user = User.objects.filter(username=username).first()
            if self.user is None:
                raise forms.ValidationError("The username is not registered.")
            if not self.user.check_password(password):
                raise forms.ValidationError("The password is incorrect.")

        return self.cleaned_data

