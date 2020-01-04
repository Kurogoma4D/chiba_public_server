from rest_framework import routers
from .views import FacilityViewSet, CategoryViewSet


router = routers.DefaultRouter()
router.register(r'facilities', FacilityViewSet)
router.register(r'categories', CategoryViewSet)
