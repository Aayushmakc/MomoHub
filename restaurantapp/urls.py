from django.urls import path
from .views import *



urlpatterns = [
    path("",index,name="index"),
    path("about/",about,name="about"),
    path("contact/",contact,name="contact"),
    path("menu/",menu,name="menu"),
    path("services/",services,name="services"),
    path('privacy/',privacy,name='privacy'),
    path('policy/',policy,name='policy'),
    path('terms/',terms,name='terms'),
    path('support/',support,name='support'),
]

