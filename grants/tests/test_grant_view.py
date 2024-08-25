from unittest.mock import patch, MagicMock
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest.mock import patch
from grants.models import Grant, GrantApplication  
from grants.serializers import GrantApplicationSerializer  

class TestApplyGrantView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.grant = Grant.objects.create(
            grant_name='Grant 1', 
            description='This is grant 1',
            grant_amount=1000,
            application_deadline='2021-12-31'
            )  
        self.url = reverse('apply_grant', kwargs={'grant_id': self.grant.id})
        self.valid_payload = {
            'user_id': 1,
            'grant_id': self.grant.id,
            'application_text': 'This is my application text',
            'submission_status': 'PENDING_REVIEW',
            'document_name': 'MyDocument',
        }

    def test_apply_grant_with_valid_pdf(self):
        pdf_file = SimpleUploadedFile("file.pdf", b"file_content", content_type="application/pdf")
        data = {**self.valid_payload, 'document': pdf_file}
        response = self.client.post(self.url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(GrantApplication.objects.count(), 1)

        self.assertEqual(GrantApplication.objects.get().document_name, 'MyDocument')

    def test_apply_grant_with_valid_doc(self):
        doc_file = SimpleUploadedFile("file.doc", b"file_content", content_type="application/msword")
        data = {**self.valid_payload, 'document': doc_file}
        response = self.client.post(self.url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(GrantApplication.objects.count(), 1)

    def test_apply_grant_with_invalid_file_type(self):
        txt_file = SimpleUploadedFile("file.txt", b"file_content", content_type="text/plain")
        data = {**self.valid_payload, 'document': txt_file}
        response = self.client.post(self.url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('2004', str(response.data))

    def test_apply_grant_with_invalid_data(self):
        invalid_payload = {
            'application_text': '', 
            'submission_status': 'PENDING_REVIEW',
        }
        response = self.client.post(self.url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def tearDown(self):
        for application in GrantApplication.objects.all():
            if application.document:
                application.document.delete(save=False)
        GrantApplication.objects.all().delete()
