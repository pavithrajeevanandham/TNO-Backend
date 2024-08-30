from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='auth_login'),

    # Add other auth-related endpoints if needed
]
