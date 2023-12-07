from django.shortcuts import render
from rest_framework import generics
from .serializers import KnittingSerializer, CrochetSerializer, SpinningSerializer, YarnSerializer, FiberSerializer, UserSerializer
from .models import Knitting, Crochet, Spinning, Yarn, Fiber
from django.contrib.auth.models import User

# Create your views here.

class UserCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserLoginView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class KnittingView(generics.ListCreateAPIView):
    queryset = Knitting.objects.all()
    serializer_class = KnittingSerializer

class KnittingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Knitting.objects.all()
    serializer_class = KnittingSerializer

class CrochetView(generics.ListCreateAPIView):
    queryset = Crochet.objects.all()
    serializer_class = CrochetSerializer

class CrochetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crochet.objects.all()
    serializer_class = CrochetSerializer

class SpinningView(generics.ListCreateAPIView):
    queryset = Spinning.objects.all()
    serializer_class = SpinningSerializer

class SpinningDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Spinning.objects.all()
    serializer_class = SpinningSerializer

class YarnView(generics.ListCreateAPIView):
    queryset = Yarn.objects.all()
    serializer_class = YarnSerializer

class YarnDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Yarn.objects.all()
    serializer_class = YarnSerializer

class FiberView(generics.ListCreateAPIView):
    queryset = Fiber.objects.all()
    serializer_class = FiberSerializer

class FiberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fiber.objects.all()
    serializer_class = FiberSerializers