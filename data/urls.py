from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views 

router = DefaultRouter()
router.register("budgets", views.BudgetViewSet, basename="budgets")
router.register("bills", views.BillViewSet, basename="bills")
router.register("todos", views.TodoViewSet, basename="todos")
router.register("events", views.EventViewSet, basename="events")

urlpatterns = [
    path("", include(router.urls)),
    path("bill-update/", views.BillUpdateAPIView.as_view(), name="bill-update"),
]