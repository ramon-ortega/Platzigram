"""User admin classes."""

#Django
from django.contrib import admin

#Models
from users.models import Profile

""" Se puede usar de esta forma """
""" admin.site.register(Profile) """

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""
    list_display = ('id', 'user', 'phone_number', 'website', 'profile_picture')
    list_display_links = ('id', 'user')
    list_editable = ('phone_number', 'website', 'profile_picture')
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'user__username', 'user__email', 'phone_number')
    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')

