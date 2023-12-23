from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.tokens import  AccessToken 

class IsAuthenticatedJWTCookie(BasePermission):
    
    def has_permission(self, request , *args):
        
        token = request.COOKIES.get("token",None)
        if token is None:
            return False
        
        token = AccessToken(token=token)
        print(token.payload)
        user = token.payload.get("user_id",None)
        if user is not None:
            return True
        
        return False
    
