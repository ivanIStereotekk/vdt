from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import User_Serializer, Picture_Serializer
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
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
from rest_framework.filters import SearchFilter



def index_view(request):
    """ Test index response view"""
    return HttpResponse(f"hello world")


@permission_classes((AllowAny,))
class Pictures_Anonymous_Api(generics.ListAPIView):
    queryset = Picture_Model.objects.all()
    serializer_class = Picture_Serializer
    ordering_fields = '-data'



@permission_classes((IsAuthenticated,))
class Pictures_Create_Api(generics.CreateAPIView):
    queryset = Picture_Model.objects.all()
    serializer_class = Picture_Serializer
    ordering_fields = '-data'

@permission_classes((IsAuthenticated,))
class Pictures_List_Create_Api(generics.ListCreateAPIView):
    queryset = Picture_Model.objects.all()
    serializer_class = Picture_Serializer
    ordering_fields = '-data'

class Pictures_Delete_View(generics.DestroyAPIView):
    queryset = Picture_Model.objects.all()
    serializer_class = Picture_Serializer
    lookup_fields = ['-data', 'tagged_people']


class Pictures_Filter_View(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Picture_Model.objects.all()
    serializer_class = Picture_Serializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filter_fields = ['description','location']
    search_fields = ['description','location']