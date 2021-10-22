from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.CharField(max_length=300)
    publisher = models.CharField(max_length=300)

class Rating(models.Model):
    book_name = models.ForeignKey(Book,related_name="rating",on_delete=models.CASCADE)
    rating_data = models.FloatField()
    date_time = models.DateTimeField(auto_now=True)

class Stock(models.Model):
    book_name = models.OneToOneField(Book,related_name="stock",on_delete=models.CASCADE, primary_key=True)
    quantity = models.IntegerField(default=0)