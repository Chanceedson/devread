from django.shortcuts import render, get_object_or_404
from .models import Book, Category

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'books/detail.html', {'book': book})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = category.books.all()
    return render(request, 'books/category_detail.html', {'category': category, 'books': books})

