from rest_framework import generics, permissions
from .serializers import LoginSerializer
# from django.contrib.auth.models import User
from .models import *


class LoginView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer
