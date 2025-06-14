from django.urls import path
from .views import About,Home
urlpatterns = [
    path('about/',About, name="about"),
    path('',Home,name="home")
]