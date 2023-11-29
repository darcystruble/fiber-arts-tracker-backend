from django.urls import path
from .views import KnittingView, CrochetView, SpinningView, YarnView, FiberView

urlpatterns = [
    path('projects/knitting/', KnittingView.as_view()),
    path('projects/crochet/', CrochetView.as_view()),
    path('projects/spinning/', SpinningView.as_view()),
    path('stash/yarn/', YarnView.as_view()),
    path('stash/fiber/', FiberView.as_view()),
]