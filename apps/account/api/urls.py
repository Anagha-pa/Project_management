from django.urls import path
from .views import *

urlpatterns = [
    
    path('users-register/', RegisterView.as_view(), name='users-register'),
    path('users-login/', UserLoginView.as_view(), name='admin_login'),
]