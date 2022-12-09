from django.contrib import admin

from rent.models import Rental, Reservation


class ReservationInline(admin.StackedInline):
    model = Reservation


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    inlines = [ReservationInline]

    class Meta:
        model = Rental


