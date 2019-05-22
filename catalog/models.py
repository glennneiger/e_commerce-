from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Movie(models.Model):
    movie_id = models.CharField(max_length=16, unique=True, primary_key=True)
    title = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    genres = models.ManyToManyField(Genre, related_name='movies', db_table='movie_genre')
    price = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title