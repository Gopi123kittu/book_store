from rest_framework import serializers
from .models import *

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("id", "book_name", "rating_data")
        #depth = 1

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('quantity', 'book_name')
        #depth = 1


class BookSerializer(serializers.ModelSerializer):
    rating = RatingSerializer(read_only=True,many=True) # adding serializer inorder to display along with book data
    stock = StockSerializer(read_only=True) # adding serializer inorde to display along with book data
    class Meta:
            model = Book
            fields = "__all__"
