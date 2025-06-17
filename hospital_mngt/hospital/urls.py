from django.urls import path
from .views import About,Home,Contact
urlpatterns = [
    path('about/',About, name="about"),
    path('',Home,name="home"),
    path('contact/', Contact, name='contact'),
]