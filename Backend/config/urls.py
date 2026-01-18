from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from events.views import EventViewSet
from organizations.views import OrganizationViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"events", EventViewSet, basename="event")
router.register(r"organizations", OrganizationViewSet, basename="organization")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
