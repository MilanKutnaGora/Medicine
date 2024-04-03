from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from record.models import Record


class RecordCreateView(CreateView):
    model = Record
    fields = ('last_name', 'name', 'surname', 'age', 'gender', 'phone','date_recorded', 'time_recorded', 'staff')
    success_url = reverse_lazy('record:list')

    def form_valid(self, form):
        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.slug = slugify(new_record.name)
            new_record.save()

        return super().form_valid(form)

class RecordUpdateView(UpdateView):
    model = Record
    fields = ('last_name', 'name', 'surname', 'age', 'gender', 'phone', 'date_recorded', 'time_recorded', 'staff')
    # success_url = reverse_lazy('record:list')

    def form_valid(self, form):
        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.slug = slugify(new_record.name)
            new_record.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('record:view', args=[self.kwargs.get('pk')])

class RecordListView(ListView):
    model = Record

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication=True)
        return queryset


class RecordDetailView(DetailView):
    model = Record



class RecordDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy('record:list')
