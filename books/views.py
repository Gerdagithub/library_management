# # from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render, redirect
# from .forms import BookForm

# def add_book(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
            
#             # Redirect to the book list page, adjust as needed
#             # return redirect('books:book_list') 
#             return render(request, 'books/add_book.html', {'form': form})
#     else:
#         form = BookForm()
#     return render(request, 'books/add_book.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import BookForm, SearchForm
from .models import Book

# print("hhhhhh")
def add_book(request):
    # print('aaaaa add_book ') 
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            print('The form of new book was saved')
            form.save()
            return redirect('books/add_book.html') # change this one later
        
        print('The form of new book was invalid')
    # print("render(request, books/add_book.html, {form: form})")
    return render(request, 'books/add_book.html', {'form': form})


# def search_books(request):
#     if request.method == 'GET':
#         search_form = SearchForm(request.GET)
#         if search_form.is_valid():
#             query = search_form.cleaned_data['search_query']
#             books = Book.objects.filter(title__icontains=query)
#             return render(request, 'books/search_results.html', {'books': books, 'search_form': search_form})
#     else:
#         search_form = SearchForm()
#     return render(request, 'books/search_books.html', {'search_form': search_form})


def search_books(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        search_field = form.cleaned_data['search_field']
        search_query = form.cleaned_data['search_query']
        books = Book.objects.filter(**{search_field + '__icontains': search_query})
        return render(request, 'search_results.html', {'books': books, 'form': form})
    else:
        form = SearchForm()
    return render(request, 'search_books.html', {'form': form})


# def update_book(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     if request.method == 'POST':
#         form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             print('The book was updated successfully')
#             return redirect('books:book_detail', book_id=book.id)  # Assume you have a detail view
#     else:
#         form = BookForm(instance=book)
#     return render(request, 'books/update_book.html', {'form': form})
