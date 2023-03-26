from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MpesaViewSet, 
    ServiceProviderViewSet, 
    MpesaTransactionViewSet,
    LipaNaMpesaGenericAPIView
)

router = DefaultRouter()
router.register("mpesa-callback-handler", MpesaViewSet, basename="mpesa-callback-handler")
router.register("service-providers", ServiceProviderViewSet, basename="service-providers")
router.register("mpesa-transactions",  MpesaTransactionViewSet, basename="mpesa-transactions")

urlpatterns = [
    path("", include(router.urls)),
    path("lipa-na-mpesa/", LipaNaMpesaGenericAPIView.as_view(), name="lipa-na-mpesa"),
]