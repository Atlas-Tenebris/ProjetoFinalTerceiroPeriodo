
from django.contrib import admin
from django.urls import path, include
from login_page import views

urlpatterns = [
    path('', views.login_page, name='login_page')
]
