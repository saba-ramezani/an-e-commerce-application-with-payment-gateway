from rest_framework import routers
from . import views


router = routers.SimpleRouter()
router.register(r'', views.ProductViewSet)

urlpatterns = router.urls