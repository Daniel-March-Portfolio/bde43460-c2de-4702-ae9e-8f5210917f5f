from rest_framework.routers import SimpleRouter

from Apartment.api_views import ApartmentViewSet

router = SimpleRouter()

router.register("", ApartmentViewSet, basename="Apartment")

urlpatterns = router.urls
