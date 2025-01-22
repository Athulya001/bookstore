from rest_framework import viewsets
from .models import Author, Genre, Book
from .serializers import AuthorSerializer, GenreSerializer, BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['title', 'author__name', 'genre__name']
    ordering_fields = ['title', 'price', 'published_date']
    ordering = ['title']

    def perform_create(self, serializer):
        # Automatically assign the current user as the author when creating a new book (optional)
        # serializer.save(author=self.request.user)
        serializer.save()

