from django.contrib import admin

from app.models import Author
from app.models import PullRequest


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    list_display = ('name', 'page_link',)
    # readonly_fields = ('name', 'page_link',)


@admin.register(PullRequest)
class PullRequestAdmin(admin.ModelAdmin):
    ordering = ('pid',)
    list_filter = (
        ('status', admin.ChoicesFieldListFilter),
        ('author', admin.RelatedFieldListFilter),
    )
    search_fields = ('title',)
    list_display = ('pid', 'status', 'title', 'author', 'link', 'scrapped_uri',)
    # readonly_fields = ('pid', 'status', 'title', 'author', 'link', 'scrapped_uri',)
