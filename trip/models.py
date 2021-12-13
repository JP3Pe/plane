from django.contrib.auth.models import User
from django.db import models


class Trip(models.Model):
    title = models.CharField(max_length=50)
    explanation = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
