from django.utils import timezone
from django.views.generic.list import ListView

from ..models import Genre


class GenreListView(ListView):
    model = Genre
    paginate_by = 25  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
