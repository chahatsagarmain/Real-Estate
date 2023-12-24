from django.shortcuts import render
from rest_framework.views import APIView
from  rest_framework.generics import ListAPIView , RetrieveAPIView
from .models import Listings
from rest_framework import permissions
from .serializers import ListingSerializer ,  ListingDetailedSerializer
from rest_framework.response import Response
from rest_framework import status
from .permission import IsAuthenticatedJWTCookie
from rest_framework.parsers import MultiPartParser,FormParser
# Create your views here.

class ListingsView(ListAPIView):
    queryset = Listings.objects.order_by("-listing_date").filter(is_published = True)
    serializer_class = ListingSerializer
    permission_classes = (permissions.AllowAny,)

class ListingsbyIdView(RetrieveAPIView):
    queryset = Listings.objects.order_by("-listing_date").filter(is_published = True)
    serializer_class = ListingDetailedSerializer
    permission_classes = (permissions.AllowAny,)
    lookup_flield = 'id'

class SearchView(APIView):
    permission_classes = (IsAuthenticatedJWTCookie,)
    parser_classes = (MultiPartParser,FormParser,)

    def post(self, request):
        
        try:

            data = request.POST
            queryset = Listings.objects.order_by('-listing_date').filter(is_published=True)
            print(data)
            published_order = data.get("published_order")

            if published_order == "Ascending":
                queryset = queryset.order_by("listing_date")
            else:
                queryset = queryset.order_by("-listing_date")

            sale_type = data.get("sale_type", None)
            if sale_type:
                queryset = queryset.filter(sale_type__iexact=sale_type)

            bedrooms = data.get("bedrooms", None)
            if bedrooms is not None:
                bedrooms = int(bedrooms.split("+")[0])
                queryset = queryset.filter(bedrooms__gte=bedrooms)

            bathrooms = data.get("bathrooms", None)
            if bathrooms is not None:
                bathrooms = int(bathrooms.split("+")[0])
                queryset = queryset.filter(bathrooms__gte=bathrooms)

            area = data.get("area", None)
            if area is not None:
                area = int(area.split("+")[0])
                queryset = queryset.filter(area__gte=area)

            home_type = data.get("home_type", None)
            if home_type is not None:
                queryset = queryset.filter(home_type__iexact=home_type)

            price = data.get("price", None)
            if price is not None:
                price = int(price.split("+")[0])
                queryset = queryset.filter(price__gte=price)

            keywords = data.get("keywords", None)
            if keywords is not None:
                queryset = queryset.filter(description__icontains=keywords)

            serialized_data = ListingDetailedSerializer(queryset, many=True)

            return Response(serialized_data.data)

        except Exception as e:
            print(str(e))
            response = {"message": str(e)}
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
