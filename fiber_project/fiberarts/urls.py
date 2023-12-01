from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('knitting/', views.KnittingView.as_view(), name='knitting_view'),
    path('knitting/<int:pk>', views.KnittingDetail.as_view(), name='knitting_detail'),
    path('crochet/', views.CrochetView.as_view(), name='crochet_view'),
    path('crochet/<int:pk>', views.CrochetDetail.as_view(), name='crochet_detail'),
    path('spinning/', views.SpinningView.as_view(), name='spinning_view'),
    path('spinning/<int:pk>', views.SpinningDetail.as_view(), name='spinning_detail'),
    path('yarn/', views.YarnView.as_view(), name='yarn_view'),
    path('yarn/<int:pk>', views.YarnDetail.as_view(), name='yarn_detail'),
    path('fiber/', views.FiberView.as_view(), name='fiber_view'),
    path('fiber/<int:pk>', views.FiberDetail.as_view(), name='fiber_detail'),
]