from rest_framework.routers import SimpleRouter

from WaterMeter.api_views import WaterMeterViewSet, WaterMeterHistoryViewSet

router = SimpleRouter()

router.register("history", WaterMeterHistoryViewSet, basename="WaterMeterHistory")
router.register("", WaterMeterViewSet, basename="WaterMeter")

urlpatterns = router.urls
