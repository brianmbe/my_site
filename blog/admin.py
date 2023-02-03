from django.contrib import admin
from .models import Author, Post, Tag

# Register your models here.


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('caption',)
    list_filter = ('caption',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)
    list_filter = ('title', 'author',)
    prepopulated_fields = {"slug": ("title", )}
