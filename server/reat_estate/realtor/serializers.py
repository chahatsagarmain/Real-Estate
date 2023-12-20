from rest_framework.serializers import ModelSerializer
from .models import Realtor

class RealtorSerializer(ModelSerializer):
    class Meta:
        model = Realtor
        fields = '__all__'