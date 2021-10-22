from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class Bookviewset(viewsets.ModelViewSet):
    '''
    This class allows book model data
    to create, edit, list the data
    
    Allowed Methods:
    
        GET, POST, PUT

    Sample Data:
    
        {
            "name": "Moon Light",
            "price": "323.00",
            "author": "abc",
            "publisher": "xyz"
        }
        

    Valid jwt token needed for the operation
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    http_method_names = ['get', 'post', 'put']
    permission_classes = [IsAuthenticated]

class Ratingviewset(viewsets.ModelViewSet):
    '''
    This class allows book Rating data
    which supports Retrieve, POST, Delete operations

    Allowed Methods:

            GET, POST, DELETE

    Sample Data:
        
        {
            "book_name": "2,  # id of the existing bookname
            "rating": 3.5
        }

    valid jwt token needed for any operaton
    '''
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    http_method_names = ['get', 'post', 'delete']
    permission_classes = [IsAuthenticated]
    
class Stockviewset(viewsets.ModelViewSet):
    '''
    This class allows stock
    which supports Retrieve, POST, Get operations

    Allowed Methods:

            GET, POST, DELETE

    Sample Data:
        
        {   
            "book_name":  1 # id of the existing book
            "quantity": 200
        }

    valid jwt token needed for any operaton
    '''
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    http_method_names = ['get', 'post', 'delete']
    permission_classes = [IsAuthenticated]
