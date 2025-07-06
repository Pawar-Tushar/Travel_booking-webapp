from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    number_of_seats = forms.IntegerField(
        label="Number of Seats",
        min_value=1, 
        widget=forms.NumberInput(attrs={
            'class': 'form-control', 
            'placeholder': 'e.g., 1 or 2', 
            'min': '1' 
        })
    )

    class Meta:
        model = Booking
        fields = ['number_of_seats']
