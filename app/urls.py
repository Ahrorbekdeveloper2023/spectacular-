from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from .views import CategoryViewSet, KlassViewSet, PraductViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register('category', CategoryViewSet)
router.register('klass', KlassViewSet)
router.register('praduct', PraductViewSet)



urlpatterns = [
    path('api/v1/', include(router.urls)),

    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('api-auth/', include('rest_framework.urls'))
]

