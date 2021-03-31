from django.shortcuts import render
from .models import Author, Book, BookInstance
from django.views import generic
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import BookForm, AuthorForm


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
    context = {
        'book_list': book_list,
    }
    return render(request, 'catalog/book_list.html', context)


def detail_authors(request):
    author_list = Author.objects.all()
    return render(request, 'catalog/author_list.html', {'author_list': author_list})


def book_detail_list(request, book_id):
    try:
        bk = Book.objects.get(id=book_id)
    except:
        raise Http404('book not found')
    return render(request, 'catalog/book_detail.html', {'book': bk})


def add_new_book(request):
    if request.method != 'POST':
        form = BookForm()
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('/books'))
    context = {'form': form}
    return render(request, 'catalog/new_book.html', context)


def add_new_author(request):
    if request.method != 'POST':
        form = AuthorForm()
    else:
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('/authors'))
    context = {'form': form}
    return render(request, 'catalog/new_author.html', context)
