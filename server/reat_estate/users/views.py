from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
# Create your views here.
User = get_user_model()

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self,request):
        data = request.data
        
        name = data.get("name",None)
        email = data.get("email",None)
        password = data.get("password",None)
        confirm_password = data.get("confirm_password",None)
        
        if password != confirm_password:
            response = {"message" : "Passwords do not match"}
            return Response(response , status=status.HTTP_400_BAD_REQUEST)
        
        if name and email and password :
            user = User.objects.filter(email = email)
            
            if user:
                response = {"message" : "User already exists"}
                return Response(response , status=status.HTTP_403_FORBIDDEN)
            
            
            if len(password) < 6 :
                    response = {"message" : "password is too short"}
                    return Response(response , status=status.HTTP_403_FORBIDDEN)
            
            
            user = User.objects.create_user(email = email , password = password , name = name)
           
            response = {"message" : "user created" ,"user_id" : user.id}
            return Response(response , status=status.HTTP_201_CREATED)
        
        else:
            response = {"message" : "missing field"}
            return Response(response , status=status.HTTP_400_BAD_REQUEST)
