from django.shortcuts import render

from .models import Book, Genre


def index(request):
    genres = Genre.objects.all()
    return render(request, 'main/index.html', {'genres': genres})

def book_list(request, slug):
    books = Book.objects.filter(genre__slug=slug)
    return  render(request, 'main/book_list.html',
                            {'books': books})
