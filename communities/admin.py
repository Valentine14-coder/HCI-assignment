from django.contrib import admin
from .models import Community

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'contact_person', 'total_residents', 'active', 'created_at')
    list_filter = ('active', 'created_at')
    search_fields = ('name', 'location', 'contact_person', 'contact_email')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Community Information', {
            'fields': ('name', 'description', 'location', 'total_residents', 'active')
        }),
        ('Contact Details', {
            'fields': ('contact_person', 'contact_email', 'contact_phone')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
