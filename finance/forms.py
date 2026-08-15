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
    "payment_source",
    "amount",
    "description",
    "date",
]

        widgets = {
            "date": forms.DateInput(
                attrs={"type": "date"}
            )
        }

from .models import Savings


class SavingsForm(forms.ModelForm):

    class Meta:
        model = Savings

        fields = [
            "transaction_type",
            "amount",
            "source",
            "date",
            "notes",
        ]

        widgets = {
            "date": forms.DateInput(
                attrs={"type": "date"}
            )
        }

        