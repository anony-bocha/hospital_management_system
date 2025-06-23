from django.urls import path
from .views import About, Home, Contact, login_view, logout_admin  # ✅ Correct imports

urlpatterns = [
    path('about/', About, name="about"),
    path('', Home, name="home"),
    path('contact/', Contact, name='contact'),
    path('admin_login/', login_view, name='login'),  # ✅ Corrected view name
    path('logout/', logout_admin, name='logout_admin'),  # ✅ Fixed case
]
