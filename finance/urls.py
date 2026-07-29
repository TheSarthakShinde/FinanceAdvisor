from django.urls import path
from . import views

urlpatterns = [
    path("income/add/", views.add_income, name="add_income"),
]