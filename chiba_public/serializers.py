from rest_framework import serializers
from .models import Facility, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class FacilitySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Facility
        fields = ('id', 'name', 'category', 'address', 'latitude', 'longitude')
