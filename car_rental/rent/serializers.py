from rest_framework import serializers
from .models import Car, Trip, Lender



class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = ['client_name', 'car', 'how_many_days', 'price_for_one_day', 'to_pay', 'start_date', 'end_date', 'lender']


class CarSerializer(serializers.ModelSerializer):
    trips = TripSerializer(many=True, required=False)

    class Meta:
        model = Car
        fields = ['model', 'price_for_a_day', 'color', 'engine_identifier', 'trips']


class LenderSerializer(serializers.ModelSerializer):
    case = TripSerializer(many=True, required=False)

    class Meta:
        model = Lender
        fields = ['lender_name', 'case']


