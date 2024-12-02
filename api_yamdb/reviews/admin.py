from django.contrib import admin

from reviews.models import Category, Comment, Genre, Review, Title


class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'year', 'category',)
    list_editable = ('category',)
    search_fields = ('genre',)
    list_filter = ('year', 'category', 'genre',)
    filter_horizontal = ('genre',)
    list_display_links = ('title',)
    empty_value_display = '-пусто-'


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug',)
    list_display_links = list_display
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug',)
    list_display_links = list_display
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Title, TitleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
admin.site.register(Review)
