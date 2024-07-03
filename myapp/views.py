from django.shortcuts import render
from .serializers import CompanySerializers,AreaSerializers,BuildingSerializers
from .permissions import CastomPermission
from .models import Company,Area,Building
from rest_framework.viewsets import ModelViewSet

class CompanyView(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers
    permission_classes = [CastomPermission]

class AreaView(ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializers
    permission_classes = [CastomPermission]

class BuildingView(ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializers
    permission_classes = [CastomPermission]