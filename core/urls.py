from django.urls import path
from core.views import dashboard, index

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("index/", index, name="index"),
]
