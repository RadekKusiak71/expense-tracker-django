import django_filters
from django import forms
from django.db import models
from .models import Expense


class ExpenseFilter(django_filters.FilterSet):
    class Meta:
        model = Expense
        exclude = ('__all__',)

        fields = {
            "category": ['exact'],
            "title": ['contains'],
            "expense_date": ['exact'],
            "price": ['gte']
        }

        filter_overrides = {
            models.DateField: {
                'filter_class': django_filters.DateFilter,
                'extra': lambda f: {
                    'widget': forms.DateInput(attrs={'type': 'date'}),
                },
            },
        }
