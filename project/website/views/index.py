import datetime

from django.shortcuts import render
from django.views import View
from website.models.author import Author
from website.models.book import Book
from website.models.work import Work


class IndexView(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        authors_count = Author.objects.count()
        works_count = Work.objects.count()
        books_count = Book.objects.count()
        dt = datetime.datetime.now()
        return render(
            request,
            self.template_name,
            context={
                "authors_count": authors_count,
                "works_count": works_count,
                "books_count": books_count,
                "updated": dt,
            },
        )
