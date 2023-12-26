"""
URL configuration for reat_estate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.urls import re_path


urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    path('admin/', admin.site.urls),
    path('api/token',TokenObtainPairView.as_view(),name='obtain-token'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='refresh-token'),
    path('api/users/',include('users.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('api/realtor/',include('realtor.urls')),
    path('api/listings/',include('listings.urls')),
    path('api/contacts/',include('contact.urls')),
    path("",TemplateView.as_view(template_name="index.html"),name="index"),
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
    
] 
