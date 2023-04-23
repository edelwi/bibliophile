from django.db import models
from django.db.models import SET_NULL

from bibliophile.website.models import Author
from bibliophile.website.models.genre import Genre


class Work(models.Model):
    title = models.CharField(max_length=400)
    authors = models.ManyToManyField(Author)
    publication_date = models.DateField("date of publication", null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=SET_NULL, null=True)
    comment = models.CharField(max_length=1000, null=True, blank=True)
    summary = models.CharField(max_length="5000", null=True, blank=True)

    def __str__(self):
        return self.title
