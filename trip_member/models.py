from django.contrib.auth.models import User
from django.db import models

from trip.models import Trip


class TripMember(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('member', 'trip')

    def __str__(self):
        return f'여행 제목: {self.trip}, 여행 멤버: {self.member}'
