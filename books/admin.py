from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.core.exceptions import ValidationError
from .models import Book
from .forms import SearchForm

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['isbn', 'title', 'author', 'publisher', 
                    'publication_date', 'genre', 'copies_in_stock']

    change_list_template = "admin/books/book/change_list.html"  # Custom change list template

    def changelist_view(self, request, extra_context=None):
        """
        Override the changelist view to include search functionality and display filtered results.
        """
        # Extract parameters from the GET request
        action = request.GET.get("action", "").strip()
        search_field = request.GET.get("search_field", "").strip()
        search_query = request.GET.get("search_query", "").strip()

        # Initialize extra_context for passing data to the template
        extra_context = extra_context or {}
        search_form = SearchForm(request.GET)  # Bind form with GET data

        # Log debugging information
        print(f"Processing changelist_view for: {request.path}")
        print(f"GET parameters: {request.GET}")

        # Determine queryset based on action
        if action == "display_all_books":
            self.filtered_queryset = self.model.objects.all()
        elif search_field and search_query:
            # Perform a search if search_field and search_query are provided
            if search_form.is_valid():
                queryset = self.model.objects.filter(
                    **{f"{search_field}__icontains": search_query}
                )
                self.filtered_queryset = queryset
            else:
                # Log form errors and set queryset to none if the form is invalid
                print("Search form is invalid:", search_form.errors)
                extra_context["form_errors"] = search_form.errors
                self.filtered_queryset = self.model.objects.none()

        # Pass the search form to the template
        extra_context["search_form"] = search_form

        # Let Django admin handle rendering the changelist with extra context
        return super().changelist_view(request, extra_context=extra_context)


    def get_queryset(self, request):
        """
        Override get_queryset to handle filtered querysets based on the search form.
        """
        if hasattr(self, 'filtered_queryset'):
            return self.filtered_queryset
        return super().get_queryset(request)


    def get_urls(self):
        """
        Add custom URLs for the admin interface.
        """
        urls = super().get_urls()
        my_urls = [
            path('search/', self.admin_site.admin_view(self.search_view), name='book_search'),
        ]
        return my_urls + urls

    
    def search_view(self, request):
        """
        Custom search view for displaying search results on a separate page.
        """
        search_form = SearchForm(request.GET)
        results = None

        if search_form.is_valid():
            field = search_form.cleaned_data['search_field']
            query = search_form.cleaned_data['search_query']
            if field and query:
                results = self.model.objects.filter(**{f'{field}__icontains': query})

        context = {
            **self.admin_site.each_context(request),
            'opts': self.model._meta,
            'search_form': search_form,
            'results': results,
        }
        return render(request, 'admin/books/book/search_results.html', context)

