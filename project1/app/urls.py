from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('contact',views.contact,name='contact'),
    path('login',views.handlelogin,name='handlelogin'),
    path('handlelogout',views.handlelogout,name='handlelogout')
]

