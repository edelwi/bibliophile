from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic.list import ListView

from ..models import Book, Work


class BookListView(ListView):
    model = Book
    paginate_by = 25  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class BookDetailView(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['related_works'] = Book.objects.filter(works__in=self.object.works.all()).all()  #.distinct()[:5]
        print(f"{self.object.pk=}")
        context['related_works'] = Work.objects.filter(book__in=[self.object.pk]).all()
        context["now"] = timezone.now()
        return context
