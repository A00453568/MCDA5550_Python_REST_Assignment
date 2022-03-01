# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import HotelSerializers
from .models import Hotel


def home(request):
    return HttpResponse("<h1>Welcome User</h1> <h2>The following functionalities are available:</h2> <ul><li><a href='/hotel_list/'>Get List of hotels</a></li> <li>Both links can be used for post request(in postman and by django rest framework): /hotel_list/ and /hotel_list/str:pk/</li> <li>To get hotel by id: '/hotel_list/id_value' For ex: <a href='/hotel_list/1'>Get Single Hotel</a></li></ul>")


@api_view(["GET", "POST"])
def Hotel_list(request):
    if request.method == "GET":
        try:
            hotel_list = Hotel.objects.all()
            hotelSerializer = HotelSerializers(hotel_list, many=True)
            return Response(hotelSerializer.data)
        except Exception:
            return Response({"Message": "List of Hotels is empty"})
    elif request.method == "POST":
        request_data = request.data
        if (Hotel.objects.filter(name=request_data['name']).exists()):
            return Response({"Message": "Hotel with this Name already exists"})
        serialize_request_data = HotelSerializers(data=request_data)
        if serialize_request_data.is_valid():
            serialize_request_data.save()
        return Response({"Message": "Hotel Added Successfully"})


@api_view(["GET", "POST"])
def Hotel_details(request, pk):
    if request.method == "GET":
        try:
            hotel_details = Hotel.objects.get(id=pk)
            hotelSerializer = HotelSerializers(hotel_details, many=False)
            return Response(hotelSerializer.data)
        except Exception:
            return Response({"Message": "No Hotel found with this id"})
    elif request.method == "POST":
        request_data = request.data
        if (Hotel.objects.filter(name=request_data['name']).exists()):
            return Response({"Message": "Hotel with this Name already exists"})
        serialize_request_data = HotelSerializers(data=request_data)
        if serialize_request_data.is_valid():
            serialize_request_data.save()
        return Response({"Message": "Hotel Added Successfully"})

