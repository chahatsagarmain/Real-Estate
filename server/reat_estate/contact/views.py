from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .serializers import ContactSerializer
from .models import Contact
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser , FormParser
from .permission import IsAuthenticatedJWTCookie
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import get_user_model
Users = get_user_model()
# Create your views here.
class SendMailView(APIView):
    parser_classes = (MultiPartParser,FormParser,)
    permission_classes = (IsAuthenticatedJWTCookie,)
    
    def post(self ,request):
        try:
            data = request.POST
            token = request.COOKIES.get("token",None)
            
            user_id = AccessToken(token=token).payload.get("user_id")
            user = Users.objects.get(id = user_id)
            raw_data = {
                "email" : user.email,
                "name" : user.name,
                "subject" : data.get("subject"),
                "message" : data.get("message")
            }
        
            serialized_data = ContactSerializer(data = raw_data)
            
            if serialized_data.is_valid():
                message = serialized_data.data.get("email") + "\n" + serialized_data.data.get("message")
                send_mail(subject=serialized_data.data.get("subject"),
                          message=message , 
                          recipient_list=["chahatsagar22003@gmail.com"],
                          from_email=settings.EMAIL_HOST_USER ,
                          )
                response = {"message" : "mail sent successfully"}
                serialized_data.create(validated_data=serialized_data.data)
                return Response(response , status=status.HTTP_200_OK)
            
            else:
                response  = {"message" : serialized_data.errors}
                return Response(response , status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            response = {"message" : str(e)}
            return Response(response , status= status.HTTP_500_INTERNAL_SERVER_ERROR)