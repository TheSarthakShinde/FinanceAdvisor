from django.urls import path
from . import views

urlpatterns = [
    path("income/add/", views.add_income, name="add_income"),
    path("expense/add/", views.add_expense, name="add_expense"),
    path("savings/add/", views.add_savings, name="add_savings"),
    path("loan/add/", views.add_loan, name="add_loan"),
    path(
    "goal/add/",
    views.add_purchase_goal,
    name="add_purchase_goal"
),path(
    "goal/<int:goal_id>/cancel/",
    views.cancel_purchase_goal,
    name="cancel_purchase_goal"
),
]