from django.db.models import Prefetch, Q
from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic.list import ListView

from ..models import Book, Work


class BookListView(ListView):
    model = Book
    paginate_by = 25  # if pagination is desired
    ordering = ["title"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class BookDetailView(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        work_objs = (
            Work.objects.filter(book__in=[self.object.pk])
            .prefetch_related(Prefetch("authors", to_attr="aftar"))
            .all()
        )
        context["related_works"] = work_objs
        context["now"] = timezone.now()
        return context


class BookSearchResultsView(ListView):
    model = Book
    paginate_by = 25  # if pagination is desired
    ordering = ["title"]
    template_name = "book_list.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        context = Book.objects.filter(
            Q(title__icontains=query) | Q(subtitle__icontains=query)
        )
        return context
