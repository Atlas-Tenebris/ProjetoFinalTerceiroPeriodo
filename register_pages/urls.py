
from django.contrib import admin
from django.urls import path, include
from register_pages import views

urlpatterns = [
    path('', views.first_page, name='first_register_page'),
    path('step2/', views.second_page, name='second_register_page'),
]
