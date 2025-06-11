from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# Define the API prefix as a variable
# You can change this to 'bpi' or any other prefix you want
API_PREFIX = getattr(settings, "API_PREFIX", "bpi")

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += [
    path(f"{API_PREFIX}/", include("app_auth.urls")),
    path(f"{API_PREFIX}/", include("app_files.urls")),
]

urlpatterns += [
    path(f"{API_PREFIX}/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        f"{API_PREFIX}/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
