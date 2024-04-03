import json

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from catalog.forms import ServiceForm, ModeratorForm
from catalog.models import Service, Category
from catalog.services import get_cached_category_for_service


def index(request):
    return render(request, 'catalog/home.html', )


def index_contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'catalog/contacts.html')

class ServiceListView(ListView):
    model = Service
    template_name = 'catalog/medicine.html'

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_published=True)

        if not self.request.user.is_staff:
            queryset = queryset.filter(owner=self.request.user)

        return queryset



class ServiceDetailView(PermissionRequiredMixin, DetailView):
    model = Service
    permission_required = 'catalog.view_service'


    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['category'] = get_cached_category_for_service()
        return context_data


def index_service(request, pk):
    category_item = Service.objects.get(pk=pk)
    context = {
        'object_list': Service.objects.filter(category_id=pk),
        'title': f'{category_item.name}'
        }

    return render(request, 'catalog/service.html', context)



class ServiceCreateView(LoginRequiredMixin, CreateView):
   model = Service
   form_class = ServiceForm
   success_url = reverse_lazy('catalog:index_medicine')

   def form_valid(self, form):
       if form.is_valid():
           new_contact = form.save()
           new_contact.personal_manager = self.request.user
           new_contact.save()
           contact_dict = {
               "Имя": new_contact.name,
               "Почта": new_contact.email
           }
           with open("contacts.json", 'a', encoding='UTF-8') as f:
               json.dump(contact_dict, f, indent=2, ensure_ascii=False)
       return super().form_valid(form)

class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('catalog:index_medicine')
    permission_required = 'catalog.change_service'



    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        if form.is_valid():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
            else:
                return self.form_invalid(form)
        return super().form_valid(form)

    def get_form_class(self):
        if self.request.user.is_staff and self.request.user.groups.filter(
                name='moderator').exists():
            return ModeratorForm
        return ServiceForm

    def test_func(self):
        _user = self.request.user
        _instance: Service = self.get_object()
        custom_perms: tuple = (
            'catalog_app.set_is_published',
            'catalog_app.set_category',
            'catalog_app.set_service_description',
        )
        if _user.is_superuser or _user == _instance.owner:
            return True
        elif _user.groups.filter(name='moderator') and _user.has_perms(custom_perms):
            return True
        return self.handle_no_permission()
