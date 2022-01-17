from django.urls import path, include
from usermodel import views
from .views import *
from allauth.account.views import LoginView

app_name = "usermodel" 

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin')
]