from django.contrib import admin
from .models import Category, Post, Comment, Likes, Subscribe

class CategoryAdmin(admin.ModelAdmin):
    fields = (
        'id', 'title', 'discription', 'photo_preview', 
    )
    list_editable = (
        'title', 
    )
    list_display = (
        'id', 'title', 'photo_preview', 
    )
    search_fields = (
        'id', 'title', 'discription', 
    )
    readonly_fields = (
        'id',
    )

class PostAdmin(admin.ModelAdmin):
    fields = (
        'id', 'title', 'text', 'category',
        'photo_preview', 'author',
    )
    list_display = (
        'id', 'title', 'category',
        'photo_preview', 'author',
    )
    search_fields = (
        'id', 'title', 'category', 'author',
    )
    readonly_fields = (
        'id',
    )


class CommentAdmin(admin.ModelAdmin):
    fields = (
        'id', 'text', 'post', 'author',
    )
    list_display = (
        'id', 'text', 'post', 'author',
    )
    search_fields = (
        'id', 'text', 'post', 'author',
    )
    readonly_fields = (
        'id',
    )

class LikesAdmin(admin.ModelAdmin):
    fields = (
        'id', 'post', 'user', 
    )
    list_editable = (
    )

    list_display = (
        'id', 'post', 'user', 
    )
    search_fields = (
        'id', 'post', 'user', 
    )
    readonly_fields = (
        'id',
    )

class SubscribeAdmin(admin.ModelAdmin):
    fields = (
        'id', 'author', 'subscriber', 
    )
    list_editable = (
    )

    list_display = (
        'id', 'author', 'subscriber', 
    )
    search_fields = (
        'id', 'author', 'subscriber', 
    )
    readonly_fields = (
        'id',
    )

admin.site.register(Subscribe, SubscribeAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Likes, LikesAdmin)