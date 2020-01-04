from rest_framework import serializers
from .models import Facility, Category
from drf_writable_nested.serializers import WritableNestedModelSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        extra_kwargs = {'id': {'read_only': False}}


class FacilitySerializer(WritableNestedModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Facility
        fields = ('id', 'name', 'category', 'address', 'latitude', 'longitude')
