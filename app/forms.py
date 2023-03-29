from django import forms
from django.forms import fields, widgets
from .models import Movie_table

class Movie_form(forms.ModelForm):
    class Meta:
        model = Movie_table
        fields = ['movie_name','director_name','release_year','movie_rating']
        
        widgets = {
            'movie_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Movie Name..'}),
            # 'thumbnail':forms.TextInput(attrs={'class':'form-control','placeholder':'URL'}),
            'director_name':forms.TextInput(attrs={'class':'form-control','placeholder':'director name'}),
            'release_year':forms.TextInput(attrs={'class':'form-control','placeholder':'Release year'}),
            'movie_rating':forms.TextInput(attrs={'class':'form-control','placeholder':'movie Rating'}),
        }