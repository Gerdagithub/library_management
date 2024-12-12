from django.shortcuts import render
from books.models import Book
from books.forms import SearchForm
from books.utils import BookSearchHandler

def home_page(request):
    # Initialize the search form
    search_form = SearchForm(request.GET)
    books = Book.objects.all()  # Default to all books
    genres = Book.objects.values_list('genre', flat=True).distinct()  # Get distinct genres

    # Check for filtering by genre
    selected_genre = request.GET.get('genre')
    if selected_genre:
        books = books.filter(genre=selected_genre)

    # Check for search functionality
    if request.GET.get('action') == 'search' and search_form.is_valid():
        search_handler = BookSearchHandler(Book, request.GET)
        search_handler.perform_search()
        search_context = search_handler.get_context()
        books = search_context.get('results', books)

    context = {
        'search_form': search_form,
        'books': books,
        'genres': genres,
        'selected_genre': selected_genre,
    }
    return render(request, 'home.html', context)