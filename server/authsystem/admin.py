from django.contrib import admin
from .models import User, ProfilePhoto

class UserAdmin(admin.ModelAdmin):
    fields = (
        'id', 'email', 'username', 'avatar', 'background',
        'name', 'lastname', 'status',
        'created', 'is_active', 'is_staff', 'is_superuser', 
    )
    list_editable = (
        'is_active', 'is_staff', 'is_superuser', 
    )
    list_display = (
        'id', 'email', 'username', 'avatar', 'background',
        'created', 'is_active', 'is_staff', 'is_superuser', 
    )
    search_fields = (
        'id', 'email', 'username', 
        'name', 'lastname', 
        'created', 'is_active', 'is_staff', 'is_superuser', 
    )
    readonly_fields = (
        'id', 'created',
    )

class ProfilePhotoAdmin(admin.ModelAdmin):
    fields = (
        'id', 'photo', 'created', 'user',
    )
    list_display = (
        'id', 'photo', 'created', 'user',
    )
    search_fields = (
        'id', 'photo', 'created', 'user',
    )
    readonly_fields = (
        'id', 'created',
    )

admin.site.register(User, UserAdmin)
admin.site.register(ProfilePhoto, ProfilePhotoAdmin)