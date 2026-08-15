from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Savings, PurchaseGoal
from .forms import (
    IncomeForm,
    ExpenseForm,
    SavingsForm,
    LoanForm,
    PurchaseGoalForm,
)
@login_required
def add_income(request):

    if request.method == "POST":

        form = IncomeForm(request.POST)

        if form.is_valid():

            income = form.save(commit=False)

            income.user = request.user

            income.save()

            return redirect("dashboard")

    else:

        form = IncomeForm()

    return render(
        request,
        "finance/add_income.html",
        {
            "form": form
        }
    )


from .forms import IncomeForm, ExpenseForm


@login_required
def add_expense(request):

    if request.method == "POST":

        form = ExpenseForm(request.POST)

        if form.is_valid():

            expense = form.save(commit=False)

            expense.user = request.user

            expense.save()
            if expense.payment_source == "SAVINGS":

                Savings.objects.create(
                    user=request.user,
                    transaction_type="WITHDRAWAL",
                    amount=expense.amount,
                    source=f"Expense: {expense.category.name}",
                    date=expense.date,
                    notes=expense.description,
                        )


            return redirect("dashboard")

    else:

        form = ExpenseForm()

    return render(
        request,
        "finance/add_expense.html",
        {
            "form": form
        }
    )
@login_required
def add_savings(request):

    if request.method == "POST":

        form = SavingsForm(request.POST)

        if form.is_valid():

            savings = form.save(commit=False)

            savings.user = request.user

            savings.save()

            return redirect("dashboard")

    else:

        form = SavingsForm()

    return render(
        request,
        "finance/add_savings.html",
        {
            "form": form
        }
    )

@login_required
def add_loan(request):

    if request.method == "POST":

        form = LoanForm(request.POST)

        if form.is_valid():

            loan = form.save(commit=False)

            loan.user = request.user

            loan.save()

            return redirect("dashboard")

    else:

        form = LoanForm()

    return render(
        request,
        "finance/add_loan.html",
        {
            "form": form
        }
    )

@login_required
def add_purchase_goal(request):

    if request.method == "POST":

        form = PurchaseGoalForm(request.POST)

        if form.is_valid():

            goal = form.save(commit=False)

            goal.user = request.user

            goal.save()

            return redirect("dashboard")

    else:

        form = PurchaseGoalForm()

    return render(
        request,
        "finance/add_purchase_goal.html",
        {
            "form": form
        }
    )


@login_required
def cancel_purchase_goal(request, goal_id):

    if request.method == "POST":

        goal = PurchaseGoal.objects.get(
            id=goal_id,
            user=request.user
        )

        goal.status = "CANCELLED"
        goal.save()

    return redirect("dashboard")