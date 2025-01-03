from django.contrib import admin
from books.models import Book,Author


# Register your models here.
class AdminBook(admin.ModelAdmin):
    list_display = ["title","published_day","ISBN","book_and_author"]
    
    empty_value_display = " -N/A- "
    
    def book_and_author(self, obj):
        for i in obj.authors.all():
            return obj.title, f'{i.first_name} {i.last_name}'
    
    search_fields = ['isbn']
    
    
class AdminAuthor(admin.ModelAdmin):
    list_display = ['first_name','last_name']
    
    
admin.site.register(Book, AdminBook)
admin.site.register(Author, AdminAuthor)
