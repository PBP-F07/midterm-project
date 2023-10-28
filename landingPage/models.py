from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta



class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)
    year_of_release = models.CharField(max_length=10)
    amount = models.IntegerField()
    borrowed_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='borrowed_books', blank=True)
    borrowed_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    is_borrowed = models.CharField(blank=True, null=True, max_length=60)

    def save(self, *args, **kwargs):
        if not self.return_date and self.borrowed_date:
            self.return_date = self.borrowed_date + timedelta(days=7)
        super(Books, self).save(*args, **kwargs) 
