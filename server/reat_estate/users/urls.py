from django.urls import path
from .views import RegisterView ,LoginView , CheckCookie

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register-user'),
    path('login/', LoginView.as_view() , name = 'login-user'),
    path('checkcookie' ,CheckCookie.as_view() , name="check-cookie")
]