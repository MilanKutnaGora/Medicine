from django.urls import path
from record.apps import RecordConfig
from record.views import RecordCreateView, RecordListView, RecordDetailView, RecordUpdateView, RecordDeleteView

app_name = RecordConfig.name

urlpatterns = [
    path('create/', RecordCreateView.as_view(), name='create'),
    path('', RecordListView.as_view(), name='list'),
    path('view/<int:pk>/', RecordDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', RecordUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', RecordDeleteView.as_view(), name='delete'),

]