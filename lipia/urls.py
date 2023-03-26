from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MpesaViewSet, ServiceProviderViewSet, MpesaTransactionViewSet

router = DefaultRouter()
router.register("lipa-na-mpesa", MpesaViewSet, basename="lipa-na-mpesa")
router.register("service-providers", ServiceProviderViewSet, basename="service-providers")
router.register("mpesa-transactions",  MpesaTransactionViewSet, basename="mpesa-transactions")

urlpatterns = [
    path("", include(router.urls))
]