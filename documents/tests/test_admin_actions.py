import pytest
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User

from documents.admin import DocumentAdmin
from documents.models import Document


@pytest.mark.django_db
def test_admin_approve_calls_notify_user(mocker):
    mock_delay = mocker.patch("documents.admin.notify_user_document_moderated.delay")

    site = AdminSite()
    admin = DocumentAdmin(Document, site)

    user = User.objects.create_user(username="u1", password="123", email="u1@mail.com")

    doc = Document.objects.create(
        user=user,
        file="documents/test.pdf",
        status=Document.Status.PENDING,
    )

    admin.approve_documents(request=None, queryset=Document.objects.filter(id=doc.id))

    doc.refresh_from_db()
    assert doc.status == Document.Status.APPROVED

    mock_delay.assert_called_once_with(doc.id)
