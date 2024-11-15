from django.db import models

# Create your models here.
class Reader(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.email})"