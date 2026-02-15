from django.contrib import admin
from .models import Author, Book, Category

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'website', 'twitter_handle')
    search_fields = ('author_name',)
    prepopulated_fields = {'slug': ('author_name',)}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_authors', 'get_categories','difficulty', 'isbn')
    #filter_horizontal = ('authors', 'categories')
    search_fields = ('title', 'author__author_name', 'category__name')
    prepopulated_fields = {'slug': ('title',)}

    # Helper method to show authors in the list view
    def get_authors(self, obj):
        return ", ".join([a.author_name for a in obj.authors.all()])
        get_authors.short_description = 'Authors'

    def get_categories(self, obj):
        return ", ".join([c.category_name for c in obj.categories.all()])
        getcategories.short_description = 'Categories'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ('category_name',)
    prepopulated_fields = {'slug': ('category_name',)}
