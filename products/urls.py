from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
# or use 'products' here for cleaner base path
router.register(r'', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
