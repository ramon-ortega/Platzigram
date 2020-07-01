""" Posts admin classes"""

# Django
from django.contrib import admin

# Models
from posts.models import Post 

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""
    list_display = ('id', 'user', 'title', 'photo')
    list_display_links = ('user',)
    list_editable = ('title', 'photo')
    search_fields = ('title', 'user', 'user__username', 'user__email', 'user__first_name', 'user__last_name')
    list_filter = ('created', 'modified')

    fieldsets = (
        ('Information',{
            'fields': (
                ('user', 'profile'),
            ),
        }),
        ('Post Info',{
            'fields': (
                ('title', 'photo'),
            ),
        }),
        ('Metadata', {
            'fields': 
                ('created', 'modified'),
        }),
    )

    readonly_fields = ('created', 'modified')

