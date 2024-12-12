from django.shortcuts import render, redirect
from .forms import BookForm, SearchForm
from .models import Book

def add_book(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            print('The form of new book was saved')
            form.save()
            return redirect('books/add_book.html') # change this one later
        print('The form of new book was invalid')
        
    return render(request, 'books/add_book.html', {'form': form})

def all_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    genres = Book.objects.values_list('genre', flat=True).distinct()

    # Check for filtering by genre
    selected_genre = request.GET.get('genre')
    if selected_genre:
        books = books.filter(genre=selected_genre)

    context = {
        'books': books,
        'genres': genres,
        'selected_genre': selected_genre,
    }
    return render(request, 'books/all_books.html', context)


