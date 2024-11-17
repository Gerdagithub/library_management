from django.contrib import admin
from loans.models import Loan


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['isbn', 'reader', 'loan_date', 'due_date', 'return_date', 'quantity', 'is_late']
    list_filter = ['loan_date', 'due_date', 'return_date']  # Remove 'is_late'
    search_fields = ['isbn__title', 'reader__name']
    readonly_fields = ['is_late']

