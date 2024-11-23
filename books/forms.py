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
        widget=forms.Select(attrs={
            'class': 'form-select me-2 w-auto fields-dropdown-menu',
            'style': 'border: 1px solid #ccc; border-radius: 5px;',
        }),
        # error_messages={
        #     'required': 'dddd'  # Suppress the error message for required field
        # },
        label="Search By" #
    )
    search_query = forms.CharField(
        max_length=255,
        error_messages={
            'required': 'sssssss'  # Suppress the error message for required field
        },
        # widget=forms.TextInput(attrs={'placeholder': 'Enter your query', 'required': 'required'}),
        # widget=forms.TextInput(attrs={'placeholder': 'Enter your query'}),  # Optional: Add placeholder
        widget=forms.TextInput(attrs={
            'class': 'form-control w-auto me-2',
            'placeholder': 'Search books...',
            # 'style': 'border: 1px solid #ccc; border-radius: 5px;',
        }),
        label="Search Query" #
    )