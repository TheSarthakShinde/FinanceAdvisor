from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import IncomeForm


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