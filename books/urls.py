from django.urls import path
from . import views

app_name = 'books'  # This is for namespacing your URLs

urlpatterns = [
    path('add/', views.add_book, name='add_book'),
    path('all-books/', views.all_books, name='all_books'), 
    # path('search/', views.search_books, name='search_books'),  # Path for a custom search view
    # Add other URL patterns for your books app here
]
