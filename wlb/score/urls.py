from rest_framework.routers import DefaultRouter

from .views import ScoreViewset

router = DefaultRouter()
router.register(r'scores', ScoreViewset, basename='score')
urlpatterns = router.urls