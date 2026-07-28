from django.db import models
from django.contrib.auth.models import User


class Income(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    source = models.CharField(max_length=100)

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.source}"


class ExpenseCategory(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name

class Expense(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        ExpenseCategory,
        on_delete=models.PROTECT
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    description = models.CharField(
        max_length=255,
        blank=True
    )

    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.category.name} - {self.amount}"


    


    