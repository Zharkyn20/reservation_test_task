from django.shortcuts import render
from django.db.models import Subquery, OuterRef

from rent.models import Reservation


def reservation_view(request):
    reservations = Reservation.objects.all().order_by('rental_id', 'checkin').annotate(
        previous_reservation=Subquery(
            Reservation.objects
            .filter(
                rental=OuterRef('rental'),
                checkin__lt=OuterRef('checkin')
            )
            .order_by('-checkin')
            .values('id')
        ))
    return render(
        request,
        "index.html",
        context={
            "reservations": reservations,
        }
    )
