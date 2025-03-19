from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import WeatherData
from .serializers import WeatherDataSerializer

@api_view(["GET"])
def get_weather_data(request):
    data = WeatherData.objects.all()
    serializer = WeatherDataSerializer(data, many=True)
    return Response(serializer.data)
