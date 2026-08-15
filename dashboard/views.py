from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from finance.models import PurchaseGoal
from recommendations.services import get_financial_summary


@login_required
def dashboard(request):

    summary = get_financial_summary(request.user)

    goals = PurchaseGoal.objects.filter(
        user=request.user,
        status="PENDING"
    ).order_by("target_date")

    return render(
        request,
        "dashboard/dashboard.html",
        {
            "summary": summary,
            "goals": goals,
        }
    )