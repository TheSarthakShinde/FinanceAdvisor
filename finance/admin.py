from django.contrib import admin
from .models import (
    Income,
    ExpenseCategory,
    Expense,
    Loan,
    Savings,
    PurchaseGoal,
)

admin.site.register(Income)
admin.site.register(ExpenseCategory)
admin.site.register(Expense)
admin.site.register(Loan)
admin.site.register(Savings)
admin.site.register(PurchaseGoal)

