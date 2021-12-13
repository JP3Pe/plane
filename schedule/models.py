from django.db import models

from trip.models import Trip


class Schedule(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    place = models.CharField(max_length=20)

    def __str__(self):
        return self.place
