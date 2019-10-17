from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('cars', views.CarListViewSet)
router.register('cars', views.CarViewSet)
router.register('trip', views.TripListViewSet)
router.register('trip', views.TripViewSet)
router.register('lender', views.LenderListViewSet)
router.register('lender', views.LenderViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]




#************************************************************************************************

# from django.conf.urls import url
# from django.contrib import admin
# from . import views
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^cars/$', views.CarList.as_view()),
#     url(r'^cars/(?P<id>(\d)+)', views.CarView.as_view()),
#     url(r'^lenders/$', views.LenderList.as_view()),
#     url(r'^lenders/(?P<id>(\d)+)', views.LenderView.as_view()),
#     url(r'^trip/$', views.TripList.as_view()),
#     url(r'^trip/(?P<id>(\d)+)', views.TripView.as_view())

# ]