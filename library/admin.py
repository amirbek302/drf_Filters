from django.contrib import admin

from library.models import Category, Book


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    name = 'library'

admin.site.register(Category, CategoryAdmin)

class BooksAdmin(admin.ModelAdmin):
    name = 'library'

admin.site.register(Book, BooksAdmin)

