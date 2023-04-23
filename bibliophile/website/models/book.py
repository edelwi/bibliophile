from django.db import models

from bibliophile.website.models import Work


class Book(models.Model):
    ELECTRONIC = "E"
    PAPER = "P"
    TYPE_CHOICES = [
        (ELECTRONIC, "Электронный"),
        (PAPER, "Бумажный")
    ]

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=1000, null=True, blank=True)
    isbn = models.CharField("ISBN", max_length=20, null=True, blank=True)
    media_type = models.CharField(max_length=1, choices=TYPE_CHOICES, default=PAPER)
    pages_number = models.IntegerField("number of pages", null=True, blank=True)
    publishing_year = models.IntegerField("the year of publishing", null=True, blank=True)
    comment = models.CharField(max_length=1000, null=True, blank=True)
    description = models.CharField(max_length="5000", null=True, blank=True)
    translator = models.CharField(max_length="100", null=True, blank=True)
    works = models.ManyToManyField(Work)
    publisher = models.CharField("publishing house", max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
