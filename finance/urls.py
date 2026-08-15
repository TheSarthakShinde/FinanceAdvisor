from django.urls import path
from . import views

urlpatterns = [
    path("income/add/", views.add_income, name="add_income"),
    path("expense/add/", views.add_expense, name="add_expense"),
    path("savings/add/", views.add_savings, name="add_savings"),
]