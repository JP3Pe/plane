from django.db import models


class Trip(models.Model):
    title = models.CharField(max_length=50)
    explanation = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title
