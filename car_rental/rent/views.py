from rest_framework import viewsets
from .serializers import CarSerializer, TripSerializer, LenderSerializer
from .models import Car, Trip, Lender


class CarViewSet (viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

class TripViewSet (viewsets.ModelViewSet):
    serializer_class = TripSerializer
    queryset = Trip.objects.all()

class LenderViewSet (viewsets.ModelViewSet):
    serializer_class = LenderSerializer
    queryset = Lender.objects.all()