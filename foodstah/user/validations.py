from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model
UserModel = get_user_model()
import re

def validate_user_signup(data):
    email = data['email'].strip().lower()
    username = data['username'].strip().lower()
    password = data['password'].strip()

    if not re.match(r"^[A-Za-z0-9_]+$", username):
        raise serializers.ValidationError("Your username must only contain letters, numbers and underscores.")
    elif (UserModel.objects.filter(username=username).exists()):
        raise serializers.ValidationError(f"The username {username} is already in use.")

    if UserModel.objects.filter(email=email).exists():
        raise serializers.ValidationError('This email is already in use.')

    if not password or len(password) < 8:
        raise serializers.ValidationError('Your password must be atleast 8 characters long.')

    return data


def validate_email(data):
    email = data['email'].strip().lower()
    if not email:
        raise ValidationError('An email is needed')
    return True

