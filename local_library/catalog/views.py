from django.shortcuts import render
from .models import Author, Book, BookInstance
from django.views import generic
from django.http import Http404


def index(request):
    """
    :return: representation home page
    """
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_instance_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    return render(request, 'index.html', context={
        'num_books': num_books,
        'num_instance': num_instance,
        'num_instance_available': num_instance_available,
        'num_authors': num_authors
    }, )


def detail(request):
    book_list = Book.objects.all()
    return render(request, 'catalog/book_list.html', {'book_list': book_list})


def detail_authors(request):
    author_list = Author.objects.all()
    return render(request, 'catalog/author_list.html', {'author_list': author_list})

def book_detail(request):
    pass