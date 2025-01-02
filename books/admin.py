from django.contrib import admin
from books.models import Book,Author

# Register your models here.
class AdminBook(admin.ModelAdmin):
    list_display = [
        'title','published_day', 'ISBN',
    ]
    
class AdminAuthor(admin.ModelAdmin):
    list_display = ['first_name','last_name']
    
    
admin.site.register(Book, AdminBook)
admin.site.register(Author, AdminAuthor)