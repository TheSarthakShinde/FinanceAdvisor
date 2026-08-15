from django import forms
from .models import Income, Expense, Savings, Loan, PurchaseGoal
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

class LoanForm(forms.ModelForm):

    class Meta:
        model = Loan

        fields = [
            "loan_name",
            "loan_type",
            "bank_name",
            "total_amount",
            "remaining_balance",
            "interest_rate",
            "emi",
            "start_date",
            "end_date",
            "status",
        ]

        widgets = {
            "start_date": forms.DateInput(
                attrs={"type": "date"}
            ),

            "end_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }

class PurchaseGoalForm(forms.ModelForm):

    class Meta:
        model = PurchaseGoal

        fields = [
            "goal_name",
            "category",
            "target_price",
            "target_date",
            "priority",
            "status",
            "notes",
        ]

        widgets = {
            "target_date": forms.DateInput(
                attrs={"type": "date"}
            )
        }

        