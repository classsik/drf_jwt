from rest_framework import serializers
from .models import Book, OrderedBooks


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class OrderedBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedBooks
        fields = '__all__'
