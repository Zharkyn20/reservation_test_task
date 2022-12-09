from django.test import TestCase
from rent.models import Rental, Reservation
from datetime import date


class HomePageTest(TestCase):

    def setUp(self):
        self.rental_1 = Rental.objects.create(name='Rental-1')
        self.rental_2 = Rental.objects.create(name='Rental-2')
        self.res_1 = Reservation.objects.create(
            rental=self.rental_1,
            checkin=date(2022, 1, 1),
            checkout=date(2022, 1, 13)
        )
        self.res_2 = Reservation.objects.create(
            rental=self.rental_1,
            checkin=date(2022, 1, 20),
            checkout=date(2022, 2, 10)
        )
        self.res_3 = Reservation.objects.create(
            rental=self.rental_1,
            checkin=date(2022, 2, 20),
            checkout=date(2022, 3, 10)
        )
        self.res_4 = Reservation.objects.create(
            rental=self.rental_2,
            checkin=date(2022, 1, 2),
            checkout=date(2022, 1, 20)
        )
        self.res_5 = Reservation.objects.create(
            rental=self.rental_2,
            checkin=date(2022, 1, 20),
            checkout=date(2022, 2, 11)
        )

    def test_reservations(self):
        response = self.client.get('/')
        reservations = Reservation.objects.all()
        prev_reservations = {1: '-', 2: 'Res-1', 3: 'Res-2', 4: '-', 5: 'Res-4'}

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['reservations']), list(reservations))
        self.assertEqual(response.context['prev_reservations'], prev_reservations)

    def test_reservations_after_deletion_one_of_them(self):
        Reservation.objects.get(pk=1).delete()
        response = self.client.get('/')
        reservations = Reservation.objects.all()
        prev_reservations = {2: '-', 3: 'Res-2', 4: '-', 5: 'Res-4'}

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['reservations']), list(reservations))
        self.assertEqual(response.context['prev_reservations'], prev_reservations)

    def test_reservations_after_adding_one_extra(self):
        reservation = Reservation.objects.create(
            rental=self.rental_1,
            checkin=date(2022, 3, 12),
            checkout=date(2022, 4, 12),
        )
        reservation.save()
        response = self.client.get('/')

        reservations = Reservation.objects.all().order_by('rental')
        prev_reservations = {1: '-', 2: 'Res-1', 3: 'Res-2', 4: '-', 5: 'Res-4', 6: 'Res-3'}

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['reservations']), list(reservations))
        self.assertEqual(response.context['prev_reservations'], prev_reservations)

