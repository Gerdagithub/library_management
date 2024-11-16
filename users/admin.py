# from django.contrib import admin

# # Register your models here.
# from .models import Reader

# admin.site.register(Reader)

from django.contrib import admin
from loans.models import Loan
from users.models import Reader


class LoanInline(admin.TabularInline):
    model = Loan
    extra = 1  # Number of empty forms to display
    fields = ['isbn', 'loan_date', 'due_date', 'return_date', 'quantity']  # Fields to display in the inline form


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number']  # Fields to display in Reader list
    inlines = [LoanInline]  # Add the Loan inline to the Reader admin
