from django.shortcuts import render
from .models import Book

def home(request):
    latest_books = Book.objects.all()[:6]
    return render(request, 'bookverse/home.html', {'latest_books': latest_books})

def about(request):
    return render(request, 'bookverse/about.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookverse/books.html', {'books': books, 'total_books': books.count()})