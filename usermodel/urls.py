from django.urls import path
from usermodel import views
from .views import *

app_name = "usermodel" 

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('signupmodal/', views.SignUpModal.as_view(), name='signup_modal'),
]