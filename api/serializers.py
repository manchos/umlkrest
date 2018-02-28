from api.models import Object
from rest_framework import serializers


class ObjectSerializer(serializers.ModelSerializer):
    distance = serializers.DecimalField(
        source='distance.m', max_digits=10, decimal_places=2,
        required=False, read_only=True
    )

    class Meta:
        model = Object
        fields = ('id', 'name', 'address', 'location', 'distance')
        read_only_fields = ('location', 'distance')