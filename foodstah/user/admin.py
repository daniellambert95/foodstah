from django.contrib import admin
from user.models import UserProfile
from rest_framework.authtoken.models import Token

admin.site.register(UserProfile)
