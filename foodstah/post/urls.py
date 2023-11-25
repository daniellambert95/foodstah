from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('api/v1/posts/', views.PostListCreateView.as_view(), name='post-list-create'),
    path('api/v1/posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
]
