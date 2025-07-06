from django.urls import path
from . import views

urlpatterns = [
    path('', views.travel_options, name='travel_options'),
    path('book/<int:pk>/', views.book_travel, name='book_travel'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('documentation/', views.documentation_view, name='documentation'),
]
