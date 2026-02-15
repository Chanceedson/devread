from django.shortcuts import render
from django.db.models import Count
from books.models import Book, Category

def index(request):
    books = Book.objects.all()[:3]
    categories = Category.objects.annotate(book_count=Count('books')).order_by('-book_count')
    return render(request, 'home/index.html', {'featured_books': books, 'categories': categories})


def about(request):
    books = Book.objects.all()
    template_data = {
        'tech_books': books
    }
    return render(request, 'home/about.html',template_data)

# Create your views here.
