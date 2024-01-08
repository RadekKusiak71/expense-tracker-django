from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Expense, Category


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField(max_length=255, required=True)
    lastname = forms.CharField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ('username', 'firstname', 'lastname',
                  'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('firstname')
        user.last_name = self.cleaned_data.get('lastname')

        if commit:
            user.save()
        return user


class CreateExpenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateExpenseForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
        self.fields['expense_date'] = forms.DateField(
            widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Expense
        exclude = ("user",)
