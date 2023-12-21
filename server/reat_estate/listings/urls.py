from django.urls import path 
from .views import ListingsView ,ListingsbyIdView, SearchView

urlpatterns = [
    path('',ListingsView.as_view()),
    path("<int:pk>",ListingsbyIdView.as_view()),
    path("search",SearchView.as_view())
]