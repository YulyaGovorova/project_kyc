from rest_framework import serializers

from docs.models import Document


class DocumentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Document,
    определяющий поля,
    которые будут сериализованы.
    """
    class Meta:
        model = Document
        fields = ('id', 'title', 'file', 'user', 'uploaded_at', 'status')