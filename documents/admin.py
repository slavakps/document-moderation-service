from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from .models import Document
from .tasks import notify_user_document_moderated


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'file_link', 'created_at', 'moderated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('id', 'user__username')
    actions = ['approve_documents', 'reject_documents']

    def approve_documents(self, request, queryset):
        queryset = queryset.filter(status=Document.Status.PENDING)
        for document in queryset:
            document.status = Document.Status.APPROVED
            document.moderated_at = timezone.now()
            document.save(update_fields=['status', 'moderated_at'])
            notify_user_document_moderated.delay(document.id)

    approve_documents.short_description = 'Подтвердить выбранные документы'

    def reject_documents(self, request, queryset):
        queryset = queryset.filter(status=Document.Status.PENDING)
        for document in queryset:
            document.status = Document.Status.REJECTED
            document.moderated_at = timezone.now()
            document.save(update_fields=['status', 'moderated_at'])
            notify_user_document_moderated.delay(document.id)

    reject_documents.short_description = 'Отклонить выбранные документы'

    def file_link(self, obj):
        if not obj.file:
            return "-"
        return format_html('<a href="{}" target="_blank">Открыть файл</a>', obj.file.url)

    file_link.short_description = "Файл"
