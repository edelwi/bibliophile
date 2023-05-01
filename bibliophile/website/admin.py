from django.contrib import admin

from .models import Genre, Author, Work, Book

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Work)
admin.site.register(Book)
# Register your models here.
