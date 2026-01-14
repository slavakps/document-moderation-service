import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_upload_requires_auth():
    client = APIClient()

    file = SimpleUploadedFile("test.pdf", b"dummy", content_type="application/pdf")

    response = client.post("/api/documents/", data={"file": file}, format="multipart")

    assert response.status_code == 401
