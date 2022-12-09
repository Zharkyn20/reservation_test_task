import datetime
import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from rent.models import Rental, Reservation


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.create_superuser()
        self.create_rentals()
        self.create_reservations()

    def create_rentals(self):
        rentals = []

        for i in range(1, 51):
            rentals.append(Rental(name=f"Rental-{i}"))

        Rental.objects.bulk_create(rentals)

    def create_reservations(self):
        reservations = []
        rentals = Rental.objects.all()

        for rental in rentals:
            start_date = datetime.date(2000, 1, 1)
            end_date = datetime.date(2022, 1, 1)

            num_days = (end_date - start_date).days
            rand_days = random.sample(range(1, num_days), 10)
            rand_dates = sorted(
                start_date + datetime.timedelta(days=day) for day in rand_days
            )

            for i in range(5):
                reservations.append(
                    Reservation(
                        rental=rental,
                        checkin=rand_dates.pop(0),
                        checkout=rand_dates.pop(0),
                    )
                )
        Reservation.objects.bulk_create(reservations)

    def create_superuser(self):
        User.objects.create_superuser(
            username="admin",
            password="admin",
        )
