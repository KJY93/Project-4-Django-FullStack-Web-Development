from django.urls import path
# 220220 include our service
from Home.views import get_index, our_service, about_us, contact_us

urlpatterns = [
    path('', get_index, name='get_index'),
    path('OurServices/', our_service, name='our_service'),
    path('AboutUs/', about_us, name='about_us'),
    path('ContactUs/', contact_us, name='contact_us')
]