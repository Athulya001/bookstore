from rest_framework import serializers
from .models import Author, Genre, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'published_date', 'author', 'genre']


def create(self, validated_data):
        # Extract the nested author and genre data
        author_data = validated_data.pop('author')
        genre_data = validated_data.pop('genre')

        # Create new author and genre if they don't already exist
        author = Author.objects.create(**author_data)
        genre = Genre.objects.create(**genre_data)

        # Now create the book instance with the author and genre
        book = Book.objects.create(author=author, genre=genre, **validated_data)

        return book