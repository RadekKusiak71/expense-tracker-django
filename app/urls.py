from django.urls import path
from .views import HomePageTempalteView, RegisterUserCreateView, ExpenseUpdateView, ExpenseDeleteView, LoginUserLoginView, ExpenseListView, ExpenseCreateView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('', HomePageTempalteView.as_view(), name='home'),
    path('register/', RegisterUserCreateView.as_view(), name='register'),
    path('login/', LoginUserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        next_page=reverse_lazy('login')), name='logout'),
    path('expense/create/', ExpenseCreateView.as_view(), name='create-expense'),
    path('expense/list/', ExpenseListView.as_view(), name='expense-list'),
    path('expense/delete/<int:pk>/',
         ExpenseDeleteView.as_view(), name='expense-delete'),
    path('expense/edit/<int:pk>/', ExpenseUpdateView.as_view(), name='expense-edit')
]
