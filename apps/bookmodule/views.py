from django.shortcuts import render
from django.db.models import Count, Q
from .models import Publisher

def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links_view(request):
    return render(request, 'bookmodule/links.html')

def text_formatting_view(request):
    return render(request, 'bookmodule/text_formatting.html')

def lab9_task6(request):  # Lab 9 - Task 6
    # Count each publisher's books with price > 50 and 1 <= quantity < 5
    publishers = Publisher.objects.annotate(
        book_count=Count(
            'book',
            filter=Q(book__price__gt=50, book__quantity__gte=1, book__quantity__lt=5)
        )
    )
    return render(request, 'bookmodule/publisherBookCount.html', {'publishers': publishers})