from django.shortcuts import render
from rest_framework import permissions
from .serializers import CompanySerializers,AreaSerializers,BuildingSerializers
from rest_framework.generics import ListCreateAPIView



