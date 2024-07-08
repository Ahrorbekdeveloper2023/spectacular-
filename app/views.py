from django.shortcuts import render
from rest_framework.viewsets  import ModelViewSet
from .models import Category, Klass, Praduct
from .serializer import CategorySerializer, KlassSerializer, PraductSerializer
from .peermissions import CategoryPermission, KlassPermission, PraductPermission



class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CategoryPermission]


class KlassViewSet(ModelViewSet):
    queryset = Klass.objects.all()
    serializer_class = KlassSerializer
    permission_classes = [KlassPermission]


class PraductViewSet(ModelViewSet):
    queryset = Praduct.objects.all()
    serializer_class = PraductSerializer
    permission_classes = [PraductPermission]