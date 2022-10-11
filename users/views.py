from urllib import response
from django import views
from django.shortcuts import render
from djoser.views import TokenCreateView

from users.models import User
from .serializers import CustomUserTokenSerializer
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.compat import coreapi, coreschema
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView
from .serializers import UserCreateSerializer
from rest_framework import status

class CustomObtainAuthTokenView(ObtainAuthToken):
    serializer_class = CustomUserTokenSerializer


class RegisterView(CreateAPIView):
    serializer_class = UserCreateSerializer
    
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        
        if not serializer.is_valid():
            return Response({
                'message': 'Could not create user.',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


        form_data = serializer.data
        form_data.pop('password')
        
        # create user
        user = User.objects.create_user(password=serializer.data['password'], **form_data)
        response_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'phone_number': user.phone_number,
        }

        headers = self.get_success_headers(serializer.data)
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
