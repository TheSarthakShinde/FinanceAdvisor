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

class Loan(models.Model):

    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("CLOSED", "Closed"),
    ]

    LOAN_TYPES = [
        ("HOME", "Home Loan"),
        ("CAR", "Car Loan"),
        ("EDUCATION", "Education Loan"),
        ("PERSONAL", "Personal Loan"),
        ("OTHER", "Other"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    loan_name = models.CharField(
        max_length=100
    )

    loan_type = models.CharField(
        max_length=20,
        choices=LOAN_TYPES
    )

    bank_name = models.CharField(
        max_length=100
    )

    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    remaining_balance = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    interest_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    emi = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    start_date = models.DateField()

    end_date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="ACTIVE"
    )

    def __str__(self):
        return f"{self.user.username} - {self.loan_name}"

class Savings(models.Model):

    TRANSACTION_TYPES = [
        ("DEPOSIT", "Deposit"),
        ("WITHDRAWAL", "Withdrawal"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    transaction_type = models.CharField(
        max_length=15,
        choices=TRANSACTION_TYPES
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    source = models.CharField(
        max_length=100
    )

    date = models.DateField()

    notes = models.CharField(
        max_length=255,
        blank=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.transaction_type} - {self.amount}"


    


    