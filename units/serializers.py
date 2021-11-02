from rest_framework import serializers

from .models import Unit


class UnitSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Unit
        fields = (
            "id",
            "name",
            "price",
            "occupied",
            "image",
            "owner"
        )
