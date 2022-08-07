from rest_framework import routers
from . import views
from django.urls import path, include


router = routers.SimpleRouter()
router.register(r'', views.OrderViewSet)

urlpatterns = [
    path('add/<str:id>/<str:token>/', views.add, name='order.add'),
    path('', include(router.urls))
]