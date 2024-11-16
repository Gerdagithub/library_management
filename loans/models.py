from django.db import models

# Create your models here.
from django.utils import timezone
from books.models import Book
from users.models import Reader

class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    isbn = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    loan_date = models.DateField(default=timezone.now)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.reader_id.name} - {self.isbn.title}"