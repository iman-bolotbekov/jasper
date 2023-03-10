from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers


class Numbo_textViewSet(viewsets.ModelViewSet):
    queryset = models.Numbo_text.objects.all()
    serializer_class = serializers.Numbo_textSerializer

