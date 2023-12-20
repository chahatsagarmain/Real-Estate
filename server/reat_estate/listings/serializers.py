from rest_framework.serializers import ModelSerializer
from .models import Listings


#Serializer for the less detailed view on home page
class ListingSerializer(ModelSerializer):
    
    class Meta:
        model = Listings
        fields = ('title','address','city','state','zipcode','price','sale_type','home_type','bedrooms','bathrooms','photo_main','area','slug')
        
    
class ListingDetailedSerializer(ModelSerializer):
    
    class Meta:
        model= Listings
        feilds = "__all__"
        lookup_field = "slug"
