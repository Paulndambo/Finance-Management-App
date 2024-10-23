from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MpesaViewSet,
    ServiceProviderViewSet,
    MpesaTransactionViewSet,
    LipaNaMpesaGenericAPIView,
    C2BConfirmationAPIView
)

router = DefaultRouter()
router.register("mpesa-callback", MpesaViewSet, basename="mpesa-callback")
router.register("service-providers", ServiceProviderViewSet, basename="service-providers")
router.register(
    "mpesa-transactions", MpesaTransactionViewSet, basename="mpesa-transactions"
)

urlpatterns = [
    path("", include(router.urls)),
    path("lipa-na-mpesa/", LipaNaMpesaGenericAPIView.as_view(), name="lipa-na-mpesa"),
    path("c2b-confirm/", C2BConfirmationAPIView.as_view(), name="c2b-confirm"),
]
