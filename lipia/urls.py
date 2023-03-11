from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MpesaViewSet

router = DefaultRouter()
router.register("lipa-na-mpesa", MpesaViewSet, basename="lipa-na-mpesa")

urlpatterns = [
    path("", include(router.urls))
]