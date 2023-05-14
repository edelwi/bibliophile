from django.db.models import Prefetch
from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic.list import ListView

from ..models import Work, Author


# class WorkListView(ListView):
#     model = Work
#     paginate_by = 25  # if pagination is desired
#     ordering = ['title']
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["now"] = timezone.now()
#         return context


class WorkGenreListView(ListView):
    model = Work
    paginate_by = 25  # if pagination is desired
    template_name = 'work_list.html'
    ordering = ['title']

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(genre_id=self.kwargs['pk']).prefetch_related(
            Prefetch('authors', to_attr='aftar')).order_by('title')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["now"] = timezone.now()
    #     return context


class WorkAuthorListView(ListView):
    model = Work
    paginate_by = 25  # if pagination is desired
    template_name = 'work_list.html'
    ordering = ['title']

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        rez = qs.filter(authors__in=[self.kwargs['pk']]).prefetch_related(
            Prefetch('authors', to_attr='aftar')).order_by('title')
        return rez


class WorkDetailView(DetailView):
    model = Work

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        authors_objs = Author.objects.filter(work__in=[self.object.pk]).all()
        context['related_authors'] = authors_objs
        context["now"] = timezone.now()
        context['back_url'] = self.request.META.get('HTTP_REFERER', "none")
        return context
