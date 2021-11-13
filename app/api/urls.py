from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    KeyCreateAPIView,
    KeyListAPIView,
    TransctionCreateAPIView,
    TransctionListAPIView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('key/new/', KeyCreateAPIView.as_view(), name="register_key"),
    path('key/', KeyListAPIView.as_view(), name="list_keys"),
    path(
        'transaction/new/', TransctionCreateAPIView.as_view(), name="make_transaction"
    ),
    path('transaction/', TransctionListAPIView.as_view(), name="list_transaction"),
]
