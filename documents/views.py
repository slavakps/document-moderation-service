from rest_framework import generics, permissions

from .models import Document
from .serializers import DocumentSerializer
from .tasks import notify_admin_new_document


class DocumentUploadView(generics.CreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        document = serializer.save(user=self.request.user)
        notify_admin_new_document.delay(document.id)
