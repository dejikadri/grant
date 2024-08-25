from django.urls import path
from users.views import (
    RegisterUser,
    UserLogin,
    Dummy
)
from grants.views import ApplyGrant

urlpatterns = [
    path('user/register', RegisterUser.as_view(), name='register_user'),
    path('user/login', UserLogin.as_view(), name='user_login'),
    path('grants/<str:grant_id>/apply', ApplyGrant.as_view(), name='apply_grant'),
    path('dummy', Dummy.as_view(), name='dummy'),
]