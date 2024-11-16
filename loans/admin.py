# from django.contrib import admin

# # Register your models here.
# from .models import Loan

# admin.site.register(Loan)

from django.contrib import admin
from loans.models import Loan


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    # list_display = ['isbn', 'reader', 'loan_date', 'due_date', 'return_date']
    # list_filter = ['loan_date', 'due_date', 'return_date']  # Optional filters
    # search_fields = ['isbn__title', 'reader__name']  # Search by book title or reader name
    # fields = ['isbn', 'reader', 'loan_date', 'due_date', 'return_date', 'quantity']  # Include quantity
    # readonly_fields = ['is_late']  # Mark 'is_late' as read-only
    list_display = ['isbn', 'reader', 'loan_date', 'due_date', 'return_date', 'quantity', 'is_late']
    list_filter = ['loan_date', 'due_date', 'return_date']  # Remove 'is_late'
    search_fields = ['isbn__title', 'reader__name']
    readonly_fields = ['is_late']

