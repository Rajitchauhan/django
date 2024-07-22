from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer




from django.shortcuts import render, get_object_or_404
from .models import Book

from django.contrib.auth.decorators import login_required
@login_required
def home(request):
    return render(request, 'booklist/home.html')

@login_required
def booklist(request):
    books = Book.objects.all()
    return render(request, 'booklist/booklist.html', {'books': books})

@login_required
def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'booklist/book_detail.html', {'book': book})
