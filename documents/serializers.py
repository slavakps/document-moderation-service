from rest_framework import serializers
from .models import Document
from django.contrib.auth.models import User


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = (
            'id',
            'file',
            'status',
            'created_at',
            'moderated_at',
        )
        read_only_fields = (
            'id',
            'status',
            'created_at',
            'moderated_at',
        )


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ("username", "email", "password")

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            password=validated_data["password"],
        )