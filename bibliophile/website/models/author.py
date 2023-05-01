from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField("date of birth", null=True, blank=True)
    death_date = models.DateField("date of death", null=True, blank=True)
    comment = models.CharField(max_length=1000, null=True, blank=True)
    biography = models.CharField(
        "short biography", max_length=5000, null=True, blank=True
    )

    def __str__(self):
        return self.name
    