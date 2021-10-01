from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('',views.index, name="index"),
    path('about',views.about,name="about"),
    path('index',views.index,name="index"),
    path('contact',views.contact,name="contact"),
]
