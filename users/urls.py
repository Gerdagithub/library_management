from django.urls import path
from . import views
from .views import home_page
from books.views import all_books

app_name = 'users'  # This is for namespacing your URLs

urlpatterns = [
    # path('', views.home_page, name='home_page'),  # Home page
    path('', home_page, name='home_page'), 
    path('/all-books', all_books, name='all_books'), 
    # path('search/', views.search_view, name='search'),
]
