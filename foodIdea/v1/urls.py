from django.urls import path

from .views import RecipeMakerViewSet, CreateUserViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('makerecipe/', RecipeMakerViewSet.as_view({'post': 'create'})),
    path('createuser/', CreateUserViewSet.as_view({'post': 'create'})),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
