from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import TravelOption, Booking
from .forms import BookingForm
from django.utils import timezone
from django.db.models import Q

def travel_options(request):
    query = request.GET.get('q')
    travel_type = request.GET.get('type')
    date = request.GET.get('date')

    options = TravelOption.objects.all()

    if query:
        options = options.filter(
            Q(source__icontains=query) | Q(destination__icontains=query)
        )
    if travel_type:
        options = options.filter(travel_type=travel_type)
    if date:
        options = options.filter(datetime__date=date)

    return render(request, 'bookings/travel_options.html', {'options': options})

@login_required
def book_travel(request, pk):
    option = get_object_or_404(TravelOption, pk=pk)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            seats = form.cleaned_data['number_of_seats']
            if seats > option.available_seats:
                form.add_error('number_of_seats', 'Not enough available seats.')
            else:
                booking = form.save(commit=False)
                booking.user = request.user
                booking.travel_option = option
                booking.total_price = option.price * seats
                booking.save()
                option.available_seats -= seats
                option.save()
                return redirect('booking_list')
    else:
        form = BookingForm()

    return render(request, 'bookings/booking_form.html', {'form': form, 'option': option})

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    if booking.status != 'Cancelled':
        booking.status = 'Cancelled'
        booking.travel_option.available_seats += booking.number_of_seats
        booking.travel_option.save()
        booking.save()
    return redirect('booking_list')


def documentation_view(request):
    return render(request, 'bookings/documentation.html')