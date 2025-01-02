from django.urls import path
from books.views import show_book_list, show_book_detail,show_author_detail

urlpatterns = [
    path('',show_book_list, name='book list'),
    path('details/<int:id>',show_book_detail, name='book detail'),
    path('details2/<int:id>',show_author_detail, name='author detail')
]

