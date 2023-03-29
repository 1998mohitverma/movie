from django.contrib import admin
from .models import Movie_table
# Register your models here.

@admin.register(Movie_table)
class Employee_admin(admin.ModelAdmin):
    list_display = ['id','movie_name','thumbnail','director_name','release_year','movie_rating']