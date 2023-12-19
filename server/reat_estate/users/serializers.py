from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"
        
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    