from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from staff.models import Staff


class StaffCreateView(CreateView):
    model = Staff
    fields = ('name', 'description', 'avatar')
    success_url = reverse_lazy('staff:list')


class StaffUpdateView(UpdateView):
    model = Staff
    fields = ('name', 'description',)
    # success_url = reverse_lazy('record:list')


    def get_success_url(self):
        return reverse('staff:view', args=[self.kwargs.get('pk')])

class StaffListView(ListView):
    model = Staff

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class StaffDetailView(DetailView):
    model = Staff


class StaffDeleteView(DeleteView):
    model = Staff
    success_url = reverse_lazy('staff:list')
