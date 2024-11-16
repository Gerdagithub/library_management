from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.core.exceptions import ValidationError
from .models import Book
from .forms import SearchForm
from books.utils import BookSearchHandler
from django.db.models.query import QuerySet
from django.utils.timezone import now, timedelta
from users.models import Reader
from loans.models import Loan

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['isbn', 'title', 'author', 'publisher', 
                    'publication_date', 'genre', 'copies_in_stock']

    change_list_template = "admin/books/book/change_list.html"  # Custom change list template
    filtered_queryset = []
    # actions = ['borrow_book_for_user']

    # def borrow_book_for_user(self, request, queryset):
    #     """
    #     Custom admin action to borrow selected books for a user.
    #     """
    #     if 'apply' in request.POST:
    #         reader_name = request.POST.get('reader_name')
    #         reader_email = request.POST.get('reader_email')
    #         reader_phone = request.POST.get('reader_phone')
            
    #         # Create or retrieve the reader
    #         reader, created = Reader.objects.get_or_create(
    #             email=reader_email,
    #             defaults={'name': reader_name, 'phone_number': reader_phone},
    #         )

    #         if created:
    #             self.message_user(request, f"New reader '{reader_name}' has been created.")

    #         # Loop through selected books and create loans
    #         for book in queryset:
    #             if book.copies_in_stock > 0:
    #                 # Calculate due date (e.g., 14 days from today)
    #                 due_date = now().date() + timedelta(days=14)

    #                 # Create the loan
    #                 Loan.objects.create(
    #                     isbn=book,
    #                     reader=reader,
    #                     due_date=due_date,
    #                 )

    #                 # Decrease book stock
    #                 book.copies_in_stock -= 1
    #                 book.save()

    #                 self.message_user(request, f"Book '{book.title}' has been loaned to {reader.name}.")
    #             else:
    #                 self.message_user(request, f"Book '{book.title}' is out of stock.", level='error')

    #         return None

    #     # Render a form to get reader details
    #     return render(request, 'admin/borrow_book_form.html', context={'books': queryset})

    # borrow_book_for_user.short_description = "Borrow selected books for a user"
    

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        search_form = SearchForm(request.GET)
        extra_context["search_form"] = search_form
        
        if request.GET != {'e': ['1']}:
            search_handler = BookSearchHandler(self.model, request.GET)
            search_handler.perform_search()
        
            new_context = search_handler.get_context()
            if new_context:
                self.filtered_queryset = new_context['results']
        else:
            self.filtered_queryset = self.filtered_queryset or self.model.objects.none() #self.model.objects.all()
            
        return super().changelist_view(request, extra_context=extra_context)


    def get_queryset(self, request):
        """
        Override get_queryset to handle filtered querysets based on the search form.
        """
        if hasattr(self, 'filtered_queryset'):
            return self.filtered_queryset
        return super().get_queryset(request)

