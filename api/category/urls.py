from rest_framework import routers
from . import views
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'', views.CategoryViewSet)

urlpatterns = router.urls