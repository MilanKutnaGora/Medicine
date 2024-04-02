from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import index, index_contacts, ServiceListView, ServiceDetailView, ServiceCreateView, ServiceUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', cache_page(60)(index), name='index'),
    path('contacts/', index_contacts, name='index_contact'),
    path('medicine/', ServiceListView.as_view(), name='index_medicine'),
    path('medicine/product/<int:pk>/', ServiceDetailView.as_view(), name='index_service'),
    path('medicine/create/', ServiceCreateView.as_view(), name='create_service'),
    path('medicine/update/<int:pk>/', ServiceUpdateView.as_view(), name='update_service'),
    path('medicine/view/<int:pk>/', ServiceDetailView.as_view(), name='view_service'),
]
