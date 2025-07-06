from django.db import models
from django.contrib.auth.models import User
import uuid

class TravelOption(models.Model):
    TYPE_CHOICES = [
        ('Flight', 'Flight'),
        ('Train', 'Train'),
        ('Bus', 'Bus'),
    ]

    travel_id = models.CharField(max_length=10, unique=True, editable=False)
    travel_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.travel_type} - {self.source} to {self.destination} on {self.datetime}"

    def save(self, *args, **kwargs):
        if not self.travel_id:
            self.travel_id = self.generate_travel_id()
        super().save(*args, **kwargs)

    def generate_travel_id(self):
        prefix = self.travel_type[0].upper()
        return f"{prefix}{uuid.uuid4().hex[:8].upper()}"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_option = models.ForeignKey(TravelOption, on_delete=models.CASCADE)
    number_of_seats = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Confirmed')

    def __str__(self):
        return f"{self.user.username} - {self.travel_option} - {self.status}"
