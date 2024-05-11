from rest_framework.routers import DefaultRouter

from .views import CreateRetrieveUser

router = DefaultRouter()
router.register(r'user', CreateRetrieveUser, basename='user')
urlpatterns = router.urls