from django.contrib import admin
from django.urls import path
from main_page import views 

#mp = Main_page
urlpatterns = [
    path ('', views.mp, name='main_page'),
]
