from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views 

router = DefaultRouter()
router.register("budgets", views.BudgetViewSet, basename="budgets")
router.register("bills", views.BillViewSet, basename="bills")
router.register("expenditures", views.ExpenditureViewSet, basename="expenditures")

urlpatterns = [
    path("", include(router.urls)),
    path("bill-update/", views.BillUpdateAPIView.as_view(), name="bill-update"),
]