from rest_framework import serializers

from models import Add


class AddSerializer(serializers.ModelSerializer):
    author = serializers.CharField(
        source='author.name',
        read_only=True
    )

    class Meta:
        model = Add
        fields = '__all__'
