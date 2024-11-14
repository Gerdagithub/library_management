from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    title = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=255, null=False)
    publisher = models.CharField(max_length=255, blank=True, null=True)  # Optional field
    publication_date = models.DateField(null=True, blank=True)  # Optional field
    genre = models.CharField(max_length=100, blank=True, null=True)  # Optional field
    copies_in_stock = models.IntegerField(default=0)  # Default to 0 if not specified

    def __str__(self):
        return f"{self.title} by {self.author}"
