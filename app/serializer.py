from rest_framework import serializers
from .models import Category, Klass, Praduct


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class KlassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klass
        fields = '__all__'


class PraductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Praduct
        fields = '__all__'