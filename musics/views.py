from django.shortcuts import render
from .models import Music
from .serializers import MusicSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class MusicViewSet(viewsets.ModelViewSet):
    queryset=Music.objects.all()
    serializer_class=MusicSerializer
    permission_classes=(IsAuthenticated,)
