from django.db import models


class Rental(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    rental = models.ForeignKey(
        "Rental", on_delete=models.PROTECT, related_name="reservations"
    )
    checkin = models.DateField()
    checkout = models.DateField()

    def __str__(self):
        return f"Res-{self.id} {self.id}"
