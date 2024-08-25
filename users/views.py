from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework import status
from users.serializer import UserSerializer
from . import user_service as srv
from common import error as err
from common import messages as msg


class RegisterUser(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = [permissions.AllowAny] 

    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')
        
        user = srv.check_user_login(email, password)
        
        if not user:
            return Response(err.get_error_response('LOGIN_FAILED'), status=status.HTTP_400_BAD_REQUEST)
        
        # Generate JWT the tokens
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({
            'refresh': str(refresh),
            'access': access_token,
            'message': msg.get_message('LOGON_SUCCESSFUL')
        }, status=status.HTTP_200_OK)

class Dummy(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def get(self, request):
        return Response({'message': 'Hello World!'})