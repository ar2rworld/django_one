from django.contrib import admin

# Register your models here.
from .models import Publisher, Book, Author, Statistics, User

class Book_Admin(admin.ModelAdmin):
  list_display = ('title', 'publisher', 'publication_date')
  list_filter = ('publisher', 'publication_date')
  ordering = ('publication_date',)
  search_fields = ('title',)

admin.site.register([Publisher, Author, User, Statistics])
admin.site.register(Book,Book_Admin)