from django import forms
from .models import Income


class IncomeForm(forms.ModelForm):

    class Meta:
        model = Income

        fields = [
            "source",
            "amount",
            "date",
        ]

        widgets = {
            "date": forms.DateInput(
                attrs={"type": "date"}
            )
        }

from .models import Expense


class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense

        fields = [
            "category",
            "amount",
            "description",
            "date",
        ]

        widgets = {
            "date": forms.DateInput(
                attrs={"type": "date"}
            )
        }