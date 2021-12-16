from django.shortcuts import render

from .models import Book

def index(request):
    books = Book.objects.filter(status='in stock')
    return render(request, 'main/index.html', {'books': books})