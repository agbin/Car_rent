from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('cars', views.CarViewSet)
router.register('trip', views.TripViewSet)
router.register('lender', views.LenderViewSet)


urlpatterns = [

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]