from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    comment = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name
