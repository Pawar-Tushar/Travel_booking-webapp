from django.contrib import admin
from .models import TravelOption, Booking

@admin.register(TravelOption)
class TravelOptionAdmin(admin.ModelAdmin):
    list_display = ('travel_id', 'travel_type', 'source', 'destination', 'datetime', 'price', 'available_seats')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'travel_option', 'number_of_seats', 'total_price', 'booking_date', 'status')
