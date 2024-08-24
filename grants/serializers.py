from rest_framework import serializers
from .models import Grant


# create serializer class for the grant model

class GrantSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    grant_name = serializers.CharField()
    grant_uuid = serializers.CharField()
    description = serializers.CharField()
    grant_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    application_deadline = serializers.DateField()
    is_active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Grant
        fields = ['grant_name', 'grant_uuid', 'description', 'grant_amount', 'application_deadline']
