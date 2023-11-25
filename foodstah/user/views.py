from django.contrib.auth import get_user_model, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserSignupSerializer, UserLoginSerializer, UserSerializer, UserProfileSerializer
from rest_framework import permissions, status
from django.contrib.auth import authenticate, login



class UserSignup(APIView):
	permission_classes = (permissions.AllowAny,)
	
	def post(self, request):
		serializer = UserSignupSerializer(data=request.data)
		if serializer.is_valid():
			user = serializer.create(serializer)
			if user:
				return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)
            response = {
                "status": status.HTTP_200_OK,
                "message": "success",
                "data": {
                    "token": token.key
                }
            }
            return Response(response, status = status.HTTP_200_OK)
        else:
            response = {
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Invalid Email or Password",
            }
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)


class UserLogout(APIView):
	permission_classes = [ IsAuthenticated ]
	
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)


class UserView(APIView):
	permission_classes = [ IsAuthenticated ]

	def get(self, request):
		serializer = UserSerializer(request.user)
		return Response({'user': serializer.data}, status=status.HTTP_200_OK)


class UserProfileView(APIView):
	permission_classes = [ IsAuthenticated ]
	# authentication_classes = (SessionAuthentication,)
	def get(self, request):
		user_serializer = UserSerializer(request.user)
		profile_serializer = UserProfileSerializer(request.user.userprofile)
		return Response({'user': user_serializer.data, 'userprofile': profile_serializer.data}, status=status.HTTP_200_OK)




# class UserSignupView(APIView):
#     def post(self, request):
#         form = UserSignupForm(request.data)

#         if form.is_valid():
#            username = form.cleaned_data.get('username')
#            email = form.cleaned_data.get('email')
#            password = form.cleaned_data.get('password1')

#            user = User.objects.create_user(username=username, email=email, password=password)
#            profile = UserProfile(user=user)
#            profile.save()

#            serializer = UserProfileSerializer(profile)
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#         print(form.errors) # print form errors
#         return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserLoginView(APIView):
#     def post(self, request):
#         form = UserLogInForm(request.data)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 token, created = Token.objects.get_or_create(user=user)
#                 return Response({'token': token.key}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'status': 'failed', 'message': 'Invalid credentials'})
#         else:
#             return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

