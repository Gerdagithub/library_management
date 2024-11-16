from django.shortcuts import render
from books.models import Book
from books.forms import SearchForm
from books.utils import BookSearchHandler

def home_page(request):
    # Initialize the search form
    search_form = SearchForm(request.GET)
    books = Book.objects.all()  # Default to all books
    
    if request.GET.get('action') == 'search' and search_form.is_valid():
        # Use the search handler to filter results
        search_handler = BookSearchHandler(Book, request.GET)
        search_handler.perform_search()
        search_context = search_handler.get_context()
        
        # Extract results if search was performed
        books = search_context.get('results', books)
    elif request.GET.get('action') == 'display_all_books':
        # Action to show all books explicitly
        books = Book.objects.all()

    context = {
        'search_form': search_form,
        'books': books,
    }
    return render(request, 'home.html', context)
