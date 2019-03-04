from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
# router.register(...)
router.register(r"voyages", VoyageViewSet)
router.register(r"ships", ShipViewSet)
router.register(r"port_vists", PortVisitViewSet)
router.register(r"transactions", TransactionViewSet)
router.register(r"sources", SourceViewSet)
router.register(r"items", ItemViewSet)
router.register(r"locations", LocationViewSet)

urlpatterns = [
    path('', default_view),
    path('api/', include(router.urls)),
    path('voyages/', VoyageListView.as_view()),
    path('voyages/<int:pk>/', VoyageDetailView.as_view()),
]

# END OF FILE
