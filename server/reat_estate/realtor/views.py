from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .models import Realtor
from .serializers import RealtorSerializer
# Create your views here.

class RealtorListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
    pagination_class = None
    
class RealtorRetrieveView(generics.RetrieveAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
    pagination_class = None
    
class TopSellerView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Realtor.objects.filter(top_seller=True)
    serializer_class = RealtorSerializer
    pagination_class = None