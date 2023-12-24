from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework_simplejwt.tokens import RefreshToken , AccessToken
# Create your views here.
User = get_user_model()

class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)
    parser_classes = (MultiPartParser,FormParser,)    
    
    def post(self,request):
        try:
            data = request.POST
        
            name = data.get("name",None)
            email = data.get("email",None)
            password = data.get("password",None)
            confirm_password = data.get("confirm_password",None)
            
            if str(password) != str(confirm_password):
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

                
                token = RefreshToken().for_user(user)
                access_token = token.access_token
                
                response = {"message" : "user created" ,"username" : user.name}
                response_obj = Response(response , status=status.HTTP_201_CREATED)
                response_obj.set_cookie(key = "token",value=access_token)
                response_obj.set_cookie(key = "role" , value="user")
                return response_obj
        
            else:
                response = {"message" : "missing field"}
                return Response(response , status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e :
            print(e)
            response = {"message" : str(e)}
            return Response(response , status=status.HTTP_400_BAD_REQUEST)
        

class LoginView(APIView):
    permission_classes = [permissions.AllowAny,]
    parser_classes = [MultiPartParser,FormParser,]
    
    def post(self,request):
        
        try:
            data = request.POST
            email = data.get("email",None)
            password = data.get("password",None)  
            
            if not email or not password :
                response = {"message" : "Enter all fields"}
                return Response(response,status=status.HTTP_400_BAD_REQUEST)
            
            user = User.objects.get(email = email)
            
            if user is None:
                print("user does not exist")
                response = {"message" :"User Does not exist"}
                return Response(response , status=status.http_404)
            
            correct_pass = user.check_password(password)
            
            if not correct_pass :
                response = {"message" : "password is not correct"}
                return Response(response , status=status.HTTP_406_NOT_ACCEPTABLE)
            
            token = RefreshToken().for_user(user)
            access_token = token.access_token
            role = "user" or user.is_staff
            
            response = {"message" : "User logged in" , "username" : user.name}
            response_obj = Response(response , status=status.HTTP_202_ACCEPTED)
            response_obj.set_cookie(key="token",value=access_token)
            response_obj.set_cookie(key="role",value=role)
            return response_obj
        
        except Exception as e:
            print(e)
            response = {"message" : str(e)}
            return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class CheckCookie(APIView):
    
    permission_classes= (permissions.AllowAny,)
    
    def get(self,request):
        try:
            token = request.COOKIES.get("token",None)
            
            if token is None:
                response = {"message" : "No token found"}
                return Response(response,status=status.HTTP_401_UNAUTHORIZED)
            
            payload = AccessToken(token=token).payload
            
            if not payload:
                response = {"message" : "No token found"}
                return Response(response,status=status.HTTP_401_UNAUTHORIZED)
            
            user_id = payload.get("user_id")
            user = User.objects.get(id=user_id)
            if user is None:
                response = {"message" : "No user found for the user id"}
                return Response(response,status=status.HTTP_404_NOT_FOUND)
            
            response = {"username" : user.name}
            print(response)
            return Response(response,status=status.HTTP_200_OK)
        
        except Exception as e:
            response = {"message" : str(e)}
            return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)