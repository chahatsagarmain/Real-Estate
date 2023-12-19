from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    
    def create_user(self , email , name , password):
        if not email :
            return ValueError("User must have an email")
        if not name :
            return  ValueError("User must have a name")
        
        user = self.model(email = email , name = name )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self , email , name , password):
        
        user = self.create_user(email=email , name = name , password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
        

class UserAccount(AbstractBaseUser,PermissionsMixin):
    
    
    email = models.EmailField(max_length = 255 , unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    
    objects = CustomUserManager() #Custom manager will called on doing UserAccount.objects.____

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def __str__(self):
        return self.name
        