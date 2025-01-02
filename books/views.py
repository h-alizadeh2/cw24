from django.shortcuts import render
from books.models import Book, Author

# Create your views here.
def show_book_list(request):
    book_list = Book.objects.all()
    # show_book = {
    #     'book':book_list
    # }
    return render(request, 'book_list.html', {'book_list':book_list})

def show_book_detail(request, id):
    book_detail = Book.objects.get(id=id)
    return render(request, 'book_detail.html', {'book_detail':book_detail})

def show_author_detail(request, id):
    author_detail = Author.objects.get(id=id)
    return render(request, 'author_detail.html', {'author_detail':author_detail})

