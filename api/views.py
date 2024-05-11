from django.shortcuts import render
from rest_framework import generics
from .models import KitabPost
from .serializers import KitabPostSerializer

class KitabPostListCreate(generics.ListCreateAPIView):
    queryset = KitabPost.objects.all()
    serializer_class = KitabPostSerializer

# Create your views here.
