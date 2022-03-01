from django.urls import path
from . import views



urlpatterns = [
    path('home/', views.home),
    path('hotel_list/', views.Hotel_list, name='hotelList'),
    path('hotel_list/<str:pk>', views.Hotel_details, name='hotelDetails'),
    path('',views.home),
]
