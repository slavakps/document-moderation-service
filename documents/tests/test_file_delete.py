import os
import tempfile
import pytest
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings
from documents.models import Document


@pytest.mark.django_db
def test_document_delete_removes_file_from_disk():
    with tempfile.TemporaryDirectory() as tmp_media:
        with override_settings(MEDIA_ROOT=tmp_media):
            user = User.objects.create_user(username="u1", password="123", email="u1@mail.com")

            doc = Document.objects.create(
                user=user,
                file=SimpleUploadedFile("test.txt", b"hello", content_type="text/plain"),
            )

            file_path = doc.file.path
            assert os.path.exists(file_path)

            doc.delete()

            assert not os.path.exists(file_path)
