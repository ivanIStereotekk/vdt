from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import User_Serializer, Picture_Serializer
from rest_framework import filters
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Picture_Model, User_Model
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from dotenv import dotenv_values
import os
from pathlib import Path

# BASE_DIR = Path('../')
# config = dotenv_values(f"{BASE_DIR}/.env")

# M O D E L S

# pip install django-filter

# Filtering to do - https://www.django-rest-framework.org/api-guide/filtering/


def index_view(request):
    """ Test index response view"""
    return HttpResponse(f"--=====----")


@permission_classes((AllowAny,))
class Pictures_Anonymous_Api(generics.ListAPIView):
    queryset = Picture_Model.objects.all()
    serializer_class = Picture_Serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '-data'


# @permission_classes((AllowAny,))
# class Person_Anonymous_Api(generics.ListAPIView):

#     queryset = User_Model.objects.all()
#     serializer_class = User_Serializer
#     filter_backends = [filters.OrderingFilter]
#     ordering_fields = '__all__'
