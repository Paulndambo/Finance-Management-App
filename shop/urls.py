from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("shops", views.ShopModelViewSet, basename="shops")
router.register("shop-stock", views.ShopStockModelViewSet, basename="shop-stock")

urlpatterns = [
    path("", include(router.urls)),
]