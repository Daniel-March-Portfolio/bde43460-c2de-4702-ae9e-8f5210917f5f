from rest_framework.routers import SimpleRouter

from Receipt.api_views import ReceiptViewSet

router = SimpleRouter()

router.register("", ReceiptViewSet, basename="Receipt")

urlpatterns = router.urls
