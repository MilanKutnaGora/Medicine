from django import forms
from django.forms import BaseInlineFormSet

from catalog.models import Service

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'is_active' or field_name == 'is_published':
                field.widget.attrs['class'] = 'form'
            else:
                field.widget.attrs['class'] = 'form-control'

class ServiceForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Service
        exclude = ('owner',)


class ModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Service
        exclude = ('name', 'description', 'price', 'date_base', 'date_change', 'owner')