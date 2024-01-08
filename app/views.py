from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, CreateExpenseForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Expense
from .filters import ExpenseFilter


class HomePageTempalteView(LoginRequiredMixin, TemplateView):
    template_name = 'base.html'


class ExpenseDeleteView(DeleteView):
    model = Expense
    success_url = reverse_lazy("expense-list")


class ExpenseCreateView(CreateView):
    model = Expense
    form_class = CreateExpenseForm
    template_name = 'expense_create.html'
    success_url = reverse_lazy('home')

    # Validation to set user for current logged in user
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ExpenseCreateView, self).form_valid(form)


class ExpenseListView(ListView):
    model = Expense
    template_name = 'expense_list.html'

    def get_queryset(self):
        qs = self.model.objects.filter(user=self.request.user)
        expense_filtered = ExpenseFilter(self.request.GET, queryset=qs)
        return expense_filtered.qs

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['expense_filtered'] = ExpenseFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


class RegisterUserCreateView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'register_page.html'
    success_url = reverse_lazy('login')


class LoginUserLoginView(LoginView):
    template_name = 'login_page.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('home')
