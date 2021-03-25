from django.db import models
from django.urls import reverse
import uuid


class Genre(models.Model):
    """
    Model representing a book genre
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre")

    def __str__(self):
        """
        :return: String for representing the Model object
        """
        return self.name


class Book(models.Model):
    """
     Model representing a book
    """
    BOOK_LANGUAGE = (
        ('ru', 'Russian'),
        ('en', 'English'),
    )

    language = models.CharField(max_length=2, choices=BOOK_LANGUAGE, blank=True, default='ru', help_text='Language of '
                                                                                                         'a book')
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character')
    genre = models.ManyToManyField(Genre, help_text='Select a genre of this book')

    # ManyToManyField used because genre can contain many books. Books can cover many genres.

    def __str__(self):
        """
        :return: String for representing the Model object
        """
        return self.title

    def get_absolute_url(self):
        """
        :return: Returns the url to access a particular book instance
        """
        return reverse('book detail', args=[str(BookInstance.id)])

    def display_genre(self):
        """
        :param self: string for the Genre.
        :return: display genre in Admin.
        """
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'


class BookInstance(models.Model):
    """
    Model representing a specific copy of a book
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        """
        :return: String for representing the Model object
        """
        return f"({self.id}, {Book.title})"


class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        """
        :return: the URL to access a particular author instance.
        """
        return reverse("author_detail", args=[str(BookInstance.id)])

    def __str__(self):
        """
        :return: String for representing the Model object
        """
        return f"({self.last_name}, {self.first_name})"


