from django.shortcuts import render
from rest_framework.views import APIView
from  rest_framework.generics import ListAPIView , RetrieveAPIView
from .models import Listings
from rest_framework import permissions
from .serializers import ListingSerializer ,  ListingDetailedSerializer
from datetime import datetime
# Create your views here.


