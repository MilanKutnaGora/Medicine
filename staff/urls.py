from django.urls import path
from staff.apps import StaffConfig

from staff.views import StaffCreateView, StaffListView, StaffDetailView, StaffUpdateView, StaffDeleteView

app_name = StaffConfig.name

urlpatterns = [
    path('create/', StaffCreateView.as_view(), name='create'),
    path('', StaffListView.as_view(), name='list'),
    path('view/<int:pk>/', StaffDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', StaffUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', StaffDeleteView.as_view(), name='delete'),

]