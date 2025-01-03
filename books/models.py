from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField('Author')
    published_day = models.DateField(auto_now_add=True)
    ISBN = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return f'{self.title} book is written by {self.authors}'
    
    
birth_date_validator = RegexValidator(
regex=r'^(19|20)\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$',
message="Enter a valid birth date in the format YYYY-MM-DD."
)    
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.DateField(validators=[birth_date_validator],)
    number_of_authored_books = models.SmallIntegerField()
    biography = models.TextField()
    
    def __str__(self):
        return f'{self.first_name}{self.last_name}'
    

class GeeksModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()

    def __str__(self):
        return self.title