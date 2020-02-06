from django.urls import path
from Home.views import get_index

urlpatterns = [
    path('', get_index, name='get_index'),
]