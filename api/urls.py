from django.urls import path
from users.views import (
    RegisterUser,
    UserLogin,
    Dummy
)
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('user/register', RegisterUser.as_view(), name='create_user'),
    path('user/login', UserLogin.as_view(), name='user_login'),
    path('user/login2', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('dummy', Dummy.as_view(), name='dummy'),
]