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


class ExpenseByYearFilter(django_filters.FilterSet):
    import datetime
    YEAR_CHOICES = [(r, r) for r in range(2015, datetime.date.today().year+1)]
    year = django_filters.ChoiceFilter(
        field_name='expense_date__year', choices=YEAR_CHOICES, label='Choose Year')

    class Meta:
        model = Expense
        exclude = ('__all__',)

        fields = {
            "expense_date": [],
        }

        filter_overrides = {
            models.DateField: {
                'filter_class': django_filters.DateFilter,
                'extra': lambda f: {
                    'widget': forms.DateInput(attrs={'type': 'date'}),
                },
            },
        }
