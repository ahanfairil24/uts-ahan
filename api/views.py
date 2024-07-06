from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import KitabPost, BabPost, FasalPost
from .serializers import KitabPostSerializer, BabPostSerializer, FasalPostSerializer

class KitabPostListCreate(generics.ListCreateAPIView):
    queryset = KitabPost.objects.all()
    serializer_class = KitabPostSerializer

    def delete(self, request):
        KitabPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class KitabPostRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = KitabPost.objects.all()
    serializer_class = KitabPostSerializer
    lookup_field = "pk"
    
class BabPostListCreate(generics.ListCreateAPIView):
    queryset = BabPost.objects.all()
    serializer_class = BabPostSerializer

    def delete(self, request):
        BabPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BabPostRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = BabPost.objects.all()
    serializer_class = BabPostSerializer
    lookup_field = "pk"   

class FasalPostListCreate(generics.ListCreateAPIView):
    queryset = FasalPost.objects.all()
    serializer_class = FasalPostSerializer

    def delete(self, request):
        FasalPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FasalPostRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = FasalPost.objects.all()
    serializer_class = FasalPostSerializer
    lookup_field = "pk"     

# Create your views here.
