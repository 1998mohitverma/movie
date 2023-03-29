from django.db import models

# Create your models here.
class Movie_table(models.Model):
    movie_name = models.CharField(max_length=70)
    thumbnail = models.TextField()
    director_name = models.CharField(max_length=50)
    release_year = models.IntegerField()
    movie_rating = models.FloatField()