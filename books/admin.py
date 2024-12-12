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
from django.contrib.admin.sites import AdminSite

# Extend the default AdminSite to include custom CSS
class CustomAdminSite(AdminSite):
    site_header = "Library Management System"
    site_title = "Library Admin"
    index_title = "Welcome to the Library Admin"
    
    def each_context(self, request):
        context = super().each_context(request)
        # Include the custom CSS
        context['custom_css'] = 'css/custom-admin.css'
        return context

custom_admin_site = CustomAdminSite(name="custom-admin")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['isbn', 'title', 'author', 'publisher', 
                    'publication_date', 'genre', 'copies_in_stock']

    # change_list_template = "admin/books/book/change_list.html"  # Custom change list template
    filtered_queryset = []

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

