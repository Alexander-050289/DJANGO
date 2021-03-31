from django import forms
from .models import Book, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['language', 'title', 'author', 'summary', 'isbn', 'genre']
        labels = {
            'language': '',
            'title': 'title of a book',
            'author': 'author',
            'summary': '',
            'isbn': '',
            'genre': '',
            }


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
        labels = {
            'first_name': 'first_name',
            'last_name': 'last_name',
            'date_of_birth': 'date_of_birth (xx/xx/xxxx)',
            'date_of_death': 'date_of_death (xx/xx/xxxx)',
        }
