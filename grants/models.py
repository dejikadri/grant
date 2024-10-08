from django.core.exceptions import ValidationError
from django.db import models
import uuid
from django.core.validators import FileExtensionValidator

# function to get 1st 12 characters of the uuid
def get_uuid():
    return str(uuid.uuid4())[:12]

def validate_file_size(file):
    limit = 10 * 1024 * 1024  # 10 MB limit
    if file.size > limit:
        raise ValidationError(_('File size should not exceed 10 MB.'))

# a model for the grant application
class Grant(models.Model):
    grant_name = models.CharField(max_length=255)
    grant_uuid = models.CharField(max_length=12, default=get_uuid, editable=False)
    description = models.TextField()
    grant_amount = models.DecimalField(max_digits=10, decimal_places=2)
    application_deadline = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class GrantApplication(models.Model):
    grant = models.ForeignKey(Grant, on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/', validators=[validate_file_size])
    document_name = models.CharField(max_length=255, null=False, blank=False)
    application_text = models.TextField(blank=False, null=False)
    submission_status = models.CharField(max_length=20, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.grant.grant_name
    
