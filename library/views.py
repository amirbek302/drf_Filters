from django.shortcuts import render
from django.template.defaultfilters import title
from rest_framework import status, generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book, Category
from .serializers import CategorySerializer, BookSerializer

# Create your views here.
# ---------------------------------------все запросы---------------------------------------------------------------
class BookAPI(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateAPI(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailAPI(generics.RetrieveAPIView):  # get by id
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateAPI(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteAPI(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BooksAPIViewByName(APIView):
    def get(self, request, title):
        books = Book.objects.filter(title__icontains=title)
        # books = Book.objects.filter(title__iexact=title)
        # books = Book.objects.filter(title__istartswith=title)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    # def patch(self, request, title):
    #     book = Book.objects.get(author__icontains=title)
    #     serializer = BookSerializer(book, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BooksAPIViewByAuthor(APIView):
    def get(self, request, author):
        books = Book.objects.filter(author__icontains=author)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    # def patch(self, request, author):
    #     book = Book.objects.get(author__icontains=author)
    #     serializer = BookSerializer(book, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BooksAPIViewByCategory(APIView):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def patch(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)