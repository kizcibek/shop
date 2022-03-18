import genres as genres
from django.shortcuts import render

from main.models import Book, Genre


def index(requests):
    genre = Genre.objects.all()
    return render(requests, 'main/index.html', {'genres': genres})
