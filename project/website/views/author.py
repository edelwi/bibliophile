from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic.list import ListView

from ..models import Author


class AuthorListView(ListView):
    model = Author
    paginate_by = 25  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class AuthorDetailView(DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
