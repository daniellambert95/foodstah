from django.urls import path
from . import views

app_name = 'group'

urlpatterns = [
    path('api/v1/groups/', views.GroupListCreateView.as_view(), name='group-list-create'),
    path('api/v1/groups/<int:pk>/', views.GroupDetailView.as_view(), name='group-detail'),
]
