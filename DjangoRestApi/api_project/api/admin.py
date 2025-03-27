from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('language',)
    save_as = True
    save_on_top = True

admin.site.register(Book, BookAdmin)
