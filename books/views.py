from django.shortcuts import render
from books.models import Book, Author

from .models import GeeksModel


# Create your views here.
def show_book_list(request):
    book_list = Book.objects.all()
    # show_book = {
    #     'book':book_list
    # }
    return render(request, 'book_list.html', {'book_list':book_list})

def show_book_detail(request, id):
    book_detail = Book.objects.get(id=id)
    author=book_detail.authors.all()
    return render(request, 'book_detail.html', {'book_detail':book_detail,'author':author})

def show_author_detail(request, id):
    author_detail = Author.objects.get(id=id)
    return render(request, 'author_detail.html', {'author_detail':author_detail})

from django.shortcuts import render

# relative import of forms


def create_view(request):
    context = {}

    
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view.html", context)