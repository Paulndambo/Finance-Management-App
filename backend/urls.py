from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Personal Finance Backend Service",
        default_version="v1",
        description="This is the personal finance backend service..",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("", include("core.urls")),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("budgets/", include("budgets.urls")),
    path("finances/", include("finances.urls")),
    path("loans/", include("loans.urls")),
    path("invoices/", include("invoices.urls")),
    path('accounts/', include('allauth.urls')),
    path("lipia/", include("lipia.urls")),
    path("integrations/", include("integrations.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
