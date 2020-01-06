import django_filters
from rest_framework import viewsets, filters

from .models import Facility, Category
from .serializers import FacilitySerializer, CategorySerializer

SEARCH_RANGE = 1.0


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.none()
    serializer_class = FacilitySerializer
    filter_fields = ('category',)

    def get_queryset(self):
        _queryset = Facility.objects.all()

        parameters = self.request.query_params
        if 'lat' in parameters and 'lng' in parameters:
            offset_lat = float(self.request.query_params['lat'])
            offset_lng = float(self.request.query_params['lng'])
            d_lat = SEARCH_RANGE / 110.9
            d_lng = SEARCH_RANGE / 91.1

            return _queryset.filter(
                latitude__lte=offset_lat+d_lat,
                latitude__gte=offset_lat-d_lat,
                longitude__lte=offset_lng+d_lng,
                longitude__gte=offset_lng-d_lng
            )

        return _queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
