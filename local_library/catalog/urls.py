from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    # path('books/', views.detail, name='detail'),
    # path('book/(?P<pk>\d+)', views.BookDetailView.as_view(), name="book-detail"),

]
