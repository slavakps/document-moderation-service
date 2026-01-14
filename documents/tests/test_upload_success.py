import pytest
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from documents.models import Document


@pytest.mark.django_db
def test_upload_document_success_calls_admin_notify(mocker):
    mock_delay = mocker.patch("documents.views.notify_admin_new_document.delay")

    user = User.objects.create_user(username="u1", password="123", email="u1@mail.com")
    token = Token.objects.create(user=user)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    file = SimpleUploadedFile("test.pdf", b"dummy", content_type="application/pdf")

    response = client.post("/api/documents/", data={"file": file}, format="multipart")

    assert response.status_code == 201
    assert response.data["status"] == Document.Status.PENDING

    mock_delay.assert_called_once()
