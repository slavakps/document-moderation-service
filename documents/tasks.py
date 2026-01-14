from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from .models import Document


@shared_task
def notify_admin_new_document(document_id: int) -> None:
    document = Document.objects.select_related('user').get(pk=document_id)

    subject = f'Новый документ от {document.user.username}'
    message = f'Пользователь {document.user.username} загрузил документ #{document.id}. Статус: {document.status}.'

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.DEFAULT_FROM_EMAIL],
        fail_silently=False,
    )
