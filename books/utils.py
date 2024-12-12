from django.core.exceptions import ValidationError
from books.forms import SearchForm

class BookSearchHandler:
    def __init__(self, model, get_params):
        """
        Initialize the handler with the model and GET parameters.
        """
        self.model = model
        self.get_params = get_params # passed request.GET 
        self.search_form = SearchForm(get_params)
        self.results = model.objects.none()  # Default to no results
        # self.filtered_queryset = self.model.objects.all()
        self.label = "All Books"


    def perform_search(self):
        """
        Validate the search form and filter the model based on the query.
        """
        if self.get_params.get("action") == "display_all_books":
            self.results = self.model.objects.all()
            return

        if self.search_form.is_valid():
            search_field = self.search_form.cleaned_data['search_field']
            search_query = self.search_form.cleaned_data['search_query']
            if search_field and search_query:
                self.results = self.model.objects.filter(
                    **{f"{search_field}__icontains": search_query}
                )
        else:
            print("Search form is invalid:", self.search_form.errors)

    def get_context(self):
        """
        Return the search form and results for use in templates.
        """            
        
        return {
            'search_form': self.search_form,
            'results': self.results,
            'label': self.label,
        }
