from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from recommendations.services import get_financial_summary


@login_required
def dashboard(request):
    summary = get_financial_summary(request.user)

    context = {
        "summary": summary
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )