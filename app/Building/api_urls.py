from rest_framework.routers import SimpleRouter

from Building.api_views import BuildingViewSet

router = SimpleRouter()

router.register("", BuildingViewSet, basename="Building")

urlpatterns = router.urls
