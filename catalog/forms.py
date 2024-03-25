from django import forms
from django.forms import BaseInlineFormSet

from catalog.models import Product

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'is_active' or field_name == 'is_published':
                field.widget.attrs['class'] = 'form'
            else:
                field.widget.attrs['class'] = 'form-control'

class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('owner',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        bad_word = ['секс', 'ИГИЛ', 'насилие', 'даллар', 'расстрел', 'бомба']

        for word in bad_word:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Недопустимые слова')

            return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        bad_word = ['секс', 'ИГИЛ', 'насилие', 'даллар', 'расстрел', 'бомба']

        for word in bad_word:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Недопустимые слова')

            return cleaned_data

class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('product',)

class ModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('product_name', 'preview', 'price', 'create_date', 'final_change_date', 'owner')