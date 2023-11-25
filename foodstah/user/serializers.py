from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from .validations import validate_user_signup

User = get_user_model()

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):
        clean_data = validate_user_signup(data)
        return clean_data

    def create(self, clean_data):
        user_obj = User.objects.create_user(
            email=clean_data['email'].value.lower(),
            password=clean_data['password'].value,
            username=clean_data['username'].value.lower()
        )
        user_profile = UserProfile.objects.create(user=user_obj)
        user_profile.save()
        return user_obj


       
class UserLoginSerializer(serializers.Serializer):
	# email = serializers.EmailField()
	username = serializers.CharField()
	password = serializers.CharField()

	def check_user(self, clean_data):
        
		user = authenticate(username=clean_data['username'].lower().strip(), password=clean_data['password'])
		if not user:
			raise serializers.ValidationError('Username or password is incorrect.')
		return user

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields = '__all__'
