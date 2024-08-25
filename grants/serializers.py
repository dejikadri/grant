from rest_framework import serializers
from .models import GrantApplication


class GrantApplicationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    grant_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    document = serializers.FileField()
    document_name = serializers.CharField()
    application_text = serializers.CharField()
    submission_status = serializers.CharField(default='PENDING_REVEIW')


    class Meta:
        model = GrantApplication
        fields = ['id', 'grant_id', 'user_id', 'document_name', 'document', 'application_text', 'submission_status']
