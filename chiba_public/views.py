import django_filters
from rest_framework import viewsets, filters

from .models import Facility, Category
from .serializers import FacilitySerializer, CategorySerializer


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
