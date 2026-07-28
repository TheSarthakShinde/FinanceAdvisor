from django.contrib import admin
from .models import Income, ExpenseCategory, Expense

admin.site.register(Income)
admin.site.register(ExpenseCategory)
admin.site.register(Expense)
