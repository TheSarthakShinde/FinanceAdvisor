from finance.models import Income, Expense, Loan, Savings, PurchaseGoal
from django.db.models import Sum
from math import ceil


def get_financial_summary(user):
    """
    Calculate the user's overall financial summary.
    """

    total_income = (
        Income.objects.filter(user=user)
        .aggregate(total=Sum("amount"))["total"] or 0
    )

    total_expenses = (
        Expense.objects.filter(user=user)
        .aggregate(total=Sum("amount"))["total"] or 0
    )

    total_emi = (
        Loan.objects.filter(user=user, status="ACTIVE")
        .aggregate(total=Sum("emi"))["total"] or 0
    )

    total_savings = (
    Savings.objects.filter(
        user=user,
        transaction_type="DEPOSIT"
    ).aggregate(total=Sum("amount"))["total"] or 0
)

    total_withdrawals = (
    Savings.objects.filter(
        user=user,
        transaction_type="WITHDRAWAL"
    ).aggregate(total=Sum("amount"))["total"] or 0
)

    current_savings = total_savings - total_withdrawals

    return {
    "income": total_income,
    "expenses": total_expenses,
    "emi": total_emi,
    "savings": current_savings,
}



def analyze_purchase_goal(user, purchase_goal):
    """
    Analyze whether a user can afford a purchase goal.
    """

    summary = get_financial_summary(user)

    income = summary["income"]
    expenses = summary["expenses"]
    emi = summary["emi"]
    savings = summary["savings"]

    disposable_income = income - expenses - emi

    # User can already afford it
    if savings >= purchase_goal.target_price:
        return {
            "can_afford": True,
            "months_required": 0,
            "message": "✅ You can afford this purchase today!"
        }

    # User has no money left every month
    if disposable_income <= 0:
        return {
            "can_afford": False,
            "months_required": None,
            "message": (
                "⚠️ Your monthly expenses and loan EMI exceed your available income. "
                "Reduce expenses or increase income before planning this purchase."
            )
        }

    remaining_amount = purchase_goal.target_price - savings

    months = ceil(remaining_amount / disposable_income)

    return {
        "can_afford": False,
        "months_required": months,
        "message": (
            f"Continue saving. "
            f"You can afford this purchase in approximately {months} month(s)."
        )
    }