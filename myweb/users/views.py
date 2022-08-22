from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import RegisterSerializer

class RegisterVirew(generics.CreateAPIView): # generics 자동 view 생성
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# Create your views here.
