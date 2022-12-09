from django.shortcuts import render

from rent.models import Reservation, Rental
from rent.utils import link_previous


def reservation_view(request):
    rentals = Rental.objects.all()
    all_reservations = Reservation.objects.none()
    prev_reservations = {}

    for rental in rentals:
        reservations = Reservation.objects.filter(rental=rental)
        all_reservations |= reservations
        prev_reservations |= link_previous(reservations)

    return render(
        request,
        'index.html',
        context={"reservations": all_reservations, 'prev_reservations': prev_reservations})


