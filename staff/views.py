from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from staff.models import Staff


class StaffCreateView(CreateView):
    model = Staff
    fields = ('name', 'description',)
    success_url = reverse_lazy('staff:list')

    # def form_valid(self, form):
    #     if form.is_valid():
    #         new_staff = form.save(commit=False)
    #         new_staff.save()
    #
    #     return super().form_valid(form)

class StaffUpdateView(UpdateView):
    model = Staff
    fields = ('name', 'description',)
    # success_url = reverse_lazy('record:list')

    # def form_valid(self, form):
    #     if form.is_valid():
    #         new_record = form.save(commit=False)
    #         new_record.save()
    #
    #     return super().form_valid(form)

    def get_success_url(self):
        return reverse('staff:view', args=[self.kwargs.get('pk')])

class StaffListView(ListView):
    model = Staff

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication=True)
        return queryset


class StaffDetailView(DetailView):
    model = Staff

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     self.object.views_count +=1
    #     self.object.save()
    #     return self.object

class StaffDeleteView(DeleteView):
    model = Staff
    success_url = reverse_lazy('staff:list')
