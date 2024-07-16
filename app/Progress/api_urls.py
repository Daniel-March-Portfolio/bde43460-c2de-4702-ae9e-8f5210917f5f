from rest_framework.routers import SimpleRouter

from Progress.api_views import ProgressRetrieve

router = SimpleRouter()

router.register("", ProgressRetrieve, basename="Progress")

urlpatterns = router.urls
