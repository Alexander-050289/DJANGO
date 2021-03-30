from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'catalog'
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.detail, name='detail'),
    path('authors/', views.detail_authors, name='detail_authors'),
    path('books/<int:book_id>', views.book_detail_list, name='book_detail_list'),

]
