# stocks/serializers.py
from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['symbol', 'price', 'upper','lower', 'frequency', 'timestamp']
