from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()


class OrderedBooks(models.Model):
    user = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    total_price = models.IntegerField()
