from rest_framework import routers
from . import views
from django.urls import path, include


router = routers.SimpleRouter()
router.register(r'', views.UserViewSet)

urlpatterns = [
    path('login/', views.signin, name='signin'),
    path('logout/<int:id>/', views.signout, name='signout'),
    path('', include(router.urls))
]