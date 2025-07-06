from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import TravelOption, Booking
from django.utils import timezone
from datetime import timedelta

class BookingTests(TestCase):
    def setUp(self):
        self.client = self.client_class()
        self.user = User.objects.create_user(username='testuser', password='TestPass123')
        self.travel_option = TravelOption.objects.create(
            travel_type='Flight',
            source='City A',
            destination='City B',
            datetime=timezone.now() + timedelta(days=1),
            price=150.00,
            available_seats=10,
        )

    def test_travel_options_list_view(self):
        response = self.client.get(reverse('travel_options'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.travel_option.source)

    def test_booking_creation(self):
        self.client.login(username='testuser', password='TestPass123')
        response = self.client.post(reverse('book_travel', args=[self.travel_option.id]), {
            'number_of_seats': 2
        })
        self.assertEqual(response.status_code, 302)
        booking = Booking.objects.get(user=self.user)
        self.assertEqual(booking.number_of_seats, 2)
        self.assertEqual(booking.total_price, 300.00)
        self.assertEqual(booking.status, 'Confirmed')
        self.travel_option.refresh_from_db()
        self.assertEqual(self.travel_option.available_seats, 8)

    def test_booking_cancellation(self):
        self.client.login(username='testuser', password='TestPass123')
        booking = Booking.objects.create(
            user=self.user,
            travel_option=self.travel_option,
            number_of_seats=2,
            total_price=300.00,
            status='Confirmed'
        )
        self.travel_option.available_seats -= 2
        self.travel_option.save()

        response = self.client.get(reverse('cancel_booking', args=[booking.id]))
        self.assertEqual(response.status_code, 302)
        booking.refresh_from_db()
        self.assertEqual(booking.status, 'Cancelled')
        self.travel_option.refresh_from_db()
        self.assertEqual(self.travel_option.available_seats, 10)
