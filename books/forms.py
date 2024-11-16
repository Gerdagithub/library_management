from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # Fields that need to be fillable by the user
        fields = ['isbn', 'title', 'author', 
                  'publisher', 'publication_date', 
                  'genre', 'copies_in_stock']
        
class SearchForm(forms.Form):
    SEARCH_CHOICES = (
        ('isbn', 'ISBN'),
        ('title', 'Title'),
        ('author', 'Author'),
        ('publisher', 'Publisher'),
    )
    search_field = forms.ChoiceField(
        choices=SEARCH_CHOICES,
        error_messages={
            'required': ''  # Suppress the error message for required field
        },
        label="Search Field" #
    )
    search_query = forms.CharField(
        max_length=255,
        error_messages={
            'required': ''  # Suppress the error message for required field
        },
        widget=forms.TextInput(attrs={'placeholder': 'Enter your query'}),  # Optional: Add placeholder
        label="Search Query" #
    )