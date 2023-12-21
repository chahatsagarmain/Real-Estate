from django.urls import path 
from .views import SendMailView

urlpatterns = [
    path("",SendMailView.as_view())
]