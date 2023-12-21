from .models import Contact
from rest_framework.serializers import ModelSerializer

class ContactSerializer(ModelSerializer):
    
    class Meta:
        model = Contact
        fields = "__all__"
        
