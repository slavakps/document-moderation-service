from django.contrib import admin

from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created_at', 'moderated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('id', 'user__username')
