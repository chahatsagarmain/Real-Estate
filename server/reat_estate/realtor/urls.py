from django.urls import path
from .views import RealtorListView , RealtorRetrieveView , TopSellerView


urlpatterns = [
    path('',RealtorListView.as_view()),
    path('topseller',TopSellerView.as_view()),
    path('<int:pk>',RealtorListView.as_view()),
]