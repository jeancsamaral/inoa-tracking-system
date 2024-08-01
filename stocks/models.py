# stocks/models.py
from django.db import models

class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    upper = models.DecimalField(max_digits=10, decimal_places=2)
    lower = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.IntegerField()  # Frequency in minutes
    timestamp = models.DateTimeField(auto_now_add=True)
    last_checked = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.symbol} - {self.price} - {self.lower} - {self.upper} - {self.frequency}"
