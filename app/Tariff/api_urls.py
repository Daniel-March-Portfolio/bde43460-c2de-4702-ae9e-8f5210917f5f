from rest_framework.routers import SimpleRouter

from Tariff.api_views import AreaTariffViewSet, WaterTariffViewSet

router = SimpleRouter()

router.register("area", AreaTariffViewSet, basename="AreaTariff")
router.register("water", WaterTariffViewSet, basename="WaterTariff")

urlpatterns = router.urls
