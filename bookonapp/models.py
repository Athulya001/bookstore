from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published_date = models.DateField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

