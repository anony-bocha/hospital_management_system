from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('about/', views.about_view, name="about"),
    path('contact/', views.contact_view, name='contact'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('index/', views.index_view, name='index'),  # Admin dashboard view
]
