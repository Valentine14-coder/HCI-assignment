from django.contrib import admin
from .models import Issue

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'issue_type', 'status', 'priority', 'location', 'created_at')
    list_filter = ('status', 'issue_type', 'priority', 'created_at')
    search_fields = ('title', 'description', 'location', 'reporter_name')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Issue Information', {
            'fields': ('title', 'description', 'issue_type', 'location', 'image')
        }),
        ('Status & Priority', {
            'fields': ('status', 'priority')
        }),
        ('Reporter Information', {
            'fields': ('reporter_name', 'reporter_email')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
