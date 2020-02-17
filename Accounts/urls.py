from django.urls import path, include
from .views import login, logout, view_profile, register

urlpatterns = [

    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('view_profile/', view_profile, name='view_profile'),
    path('register/', register, name='register'),
]