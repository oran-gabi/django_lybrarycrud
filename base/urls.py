
########### aplication ###########
from atexit import register
from django.contrib import admin
from django.urls import path
from django.urls import path
from .views import product,register, index, test
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView



urlpatterns = [
    path('', views.index),
    path('test', views.test),
    path('member', views.member),
    path('pub', views.allpub),
    path('product/', product, name='product-list'),     # For GET all and POST requests
    path('product/<int:id>/', product, name='product-detail'),  # For GET, PUT, PATCH, DELETE by id
    path('login/', TokenObtainPairView.as_view()),
    path('register/', register, name='register'),  # Register endpoint

]
