from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('api/v1/auth/signup/', views.UserSignup.as_view(), name='user-signup'),
    path('api/v1/auth/login/', views.UserLogin.as_view(), name='user-login'),
    path('api/v1/auth/logout/', views.UserLogout.as_view(), name='user-logout'),
    path('api/v1/auth/user/', views.UserView.as_view(), name='user'),
    path('api/v1/auth/userprofile/', views.UserProfileView.as_view(), name='userprofile'),
]
