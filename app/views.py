from django.shortcuts import redirect, render
from .models import Movie_table
from .forms import Movie_form
from django.contrib import messages
import imdb
# Create your views here.

def home_page(request):
    return render(request, 'home.html')

def add_movie(request):
    if request.method=='POST':
        form = Movie_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Movie Add successfully!!!')
            form = Movie_form()
    else:
        form = Movie_form()
    return render(request, 'add.html',{'form':form})

def show_movies(request):
    stud = Movie_table.objects.all()
    return render(request, 'show.html',{'stu':stud})

def update_movie(request, id):
    if request.method == 'POST':
        pi = Movie_table.objects.get(pk=id)
        form = Movie_form(request.POST,instance=pi)
        if form.is_valid():
            form.save()
            messages.success(request,'Movie Updated successfully')
    else:
        pi = Movie_table.objects.get(pk=id)
        form = Movie_form(instance=pi)
    return render(request, 'update.html',{'form':form})

def delete_movie(request, id):
    if request.method == 'POST':
        pi = Movie_table.objects.get(pk=id)
        pi.delete()
        return redirect('/show/')

def search_movie(request):
    given = request.POST['name']
    emp = Movie_table.objects.filter(movie_name__iexact=given)
    if emp:
        return render(request, 'show.html',{'stu':emp})
    else:
        search_data = imdb.IMDb()
        search_movie_name = request.POST['name']
        search_results = search_data.search_movie(search_movie_name)
        if search_results:
            try:
                movie = search_results[0]
                # get the title, cover image URL, year, and director
                search_data.update(movie)
                movie_name = movie['title']
                thumbnail = movie['cover url']
                release_year = movie['year']
                director_name = movie['director'][0]['name']
                actor_name = movie['cast'][0]['name']
                movie_rating = movie['rating']

                movie_dict = {
                    "movie_name": movie_name,
                    "actor_name": actor_name,
                    "director_name": director_name,
                    "thumbnail": thumbnail,
                    "release_year": release_year,
                    "movie_rating": movie_rating
                }
                return render(request, 'imdb.html',{"movie":movie_dict})    
            except:
                return render(request, 'imdb.html')         
    return render(request, 'imdb.html',{'stu':emp})    