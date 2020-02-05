from django.urls import path, include
from .views import login, logout, profile, register

urlpatterns = [
    path('', include('Catalog.urls')),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
]