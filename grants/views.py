from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from grants.serializers import GrantApplicationSerializer
from common import error as err

class ApplyGrant(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, grant_id):
        uploaded_file = request.FILES.get('document')  
        if uploaded_file:
            file_extension = uploaded_file.name.split('.')[-1].lower()
            if file_extension not in ['pdf', 'doc', 'docx']:
                return Response(
                    err.get_error_response('INVALID_DOCUMENT_TYPE'),
                    status=status.HTTP_400_BAD_REQUEST
                )

        data = request.data
        data['grant_id'] = grant_id
        serializer = GrantApplicationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    