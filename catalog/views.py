import json

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm, ModeratorForm
from catalog.models import Product, Version
# from catalog.services import get_cached_category_for_product


def index(request):
    return render(request, 'catalog/home.html', )

def index_contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'catalog/contacts.html')

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/shop.html'

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_published=True)

        if not self.request.user.is_staff:
            queryset = queryset.filter(owner=self.request.user)

        return queryset



class ProductDetailView(PermissionRequiredMixin, DetailView):
    model = Product
    permission_required = 'catalog.view_product'


    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data['category'] = get_cached_category_for_product()
    #     return context_data


def index_product(request, pk):
    category_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'{category_item.name}'
        }

    return render(request, 'catalog/product.html', context)



class ProductCreateView(LoginRequiredMixin, CreateView):
   model = Product
   form_class = ProductForm
   success_url = reverse_lazy('catalog:index_shop')

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

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index_shop')
    permission_required = 'catalog.change_product'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1,)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context_data['formset'] = formset
        return context_data

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
        return ProductForm

    def test_func(self):
        _user = self.request.user
        _instance: Product = self.get_object()
        custom_perms: tuple = (
            'catalog_app.set_is_published',
            'catalog_app.set_category',
            'catalog_app.set_product_description',
        )
        if _user.is_superuser or _user == _instance.owner:
            return True
        elif _user.groups.filter(name='moderator') and _user.has_perms(custom_perms):
            return True
        return self.handle_no_permission()
