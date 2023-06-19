from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import RecipeMakerViewSet, CreateUserViewSet

router = routers.SimpleRouter()

router.register(r'recipe', RecipeMakerViewSet, basename='recipe')
router.register(r'createuser', CreateUserViewSet, basename='createuser')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"
    ),
    path("doc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

urlpatterns += router.urls