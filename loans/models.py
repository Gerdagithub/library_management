from django.db import models
from django.utils.timezone import now, timedelta
from books.models import Book
from users.models import Reader

class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    isbn = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    loan_date = models.DateField(default=now)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Automatically set due_date if not provided
        if not self.due_date:
            self.due_date = now().date() + timedelta(days=14)
            
            
            
            
            
        # # Check if there are enough copies in stock
        # if self.isbn.copies_in_stock < self.quantity:
        #     raise ValueError(f"Not enough copies of '{self.isbn.title}' in stock.")
        
        # is_return_date_specified = False
        # Check if this is an update or a new loan
        if self.pk:  # Check if the instance already exists in the database
            # Fetch the existing loan from the database
            existing_loan = Loan.objects.get(pk=self.pk)
            previous_quantity = existing_loan.quantity
            # if existing_loan.return_date:
            #     is_return_date_specified = True
            if self.return_date:
                self.isbn.copies_in_stock += previous_quantity
                self.isbn.save()
            
        if not self.pk or not self.return_date:
            # This is a new loan
            previous_quantity = 0

            # Calculate the change in quantity
            quantity_difference = self.quantity - previous_quantity

            # Deduct quantity from book stock if quantity_difference is positive
            # if quantity_difference > 0:
            if self.isbn.copies_in_stock < quantity_difference:
                raise ValueError(f"Not enough copies of '{self.isbn.title}' in stock.")
            
            self.isbn.copies_in_stock -= quantity_difference
            self.isbn.save()
            
        
        
        
        
        # # Deduct quantity from book stock
        # self.isbn.copies_in_stock -= self.quantity
        # self.isbn.save()
        
        super().save(*args, **kwargs)
        
    @property
    def is_late(self):
        """
        Determines if the user is late in returning the book.
        - Returns True if the current date is past the due_date and the book has not been returned.
        - Returns False otherwise.
        """
        if self.return_date:
            return self.return_date > self.due_date
        # return now().date() > self.due_date
        return False

    def __str__(self):
        return f"{self.reader.name} - {self.isbn.title} (x{self.quantity})"
    # def __str__(self):
    #     return f"{self.reader.name} - {self.isbn.title}"
