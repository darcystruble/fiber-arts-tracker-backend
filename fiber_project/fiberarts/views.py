from django.shortcuts import render
from rest_framework import generics
from .serializers import KnittingSerializer, CrochetSerializer, SpinningSerializer, YarnSerializer, FiberSerializer
from .models import Knitting, Crochet, Spinning, Yarn, Fiber

# Create your views here.

class KnittingView(generics.ListAPIView):
    queryset = Knitting.objects.all()
    serializer_class = KnittingSerializer

class CrochetView(generics.ListAPIView):
    queryset = Crochet.objects.all()
    serializer_class = CrochetSerializer

class SpinningView(generics.ListAPIView):
    queryset = Spinning.objects.all()
    serializer_class = SpinningSerializer

class YarnView(generics.ListAPIView):
    queryset = Yarn.objects.all()
    serializer_class = YarnSerializer

class FiberView(generics.ListAPIView):
    queryset = Fiber.objects.all()
    serializer_class = FiberSerializer