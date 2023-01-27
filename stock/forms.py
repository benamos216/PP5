from django import forms
from .models import Stock, Category


class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = '__all__'
