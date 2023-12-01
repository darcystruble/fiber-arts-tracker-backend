from rest_framework import serializers
from .models import Knitting, Crochet, Spinning, Yarn, Fiber

class KnittingSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Knitting
        fields = ('id', 'user', 'name', 'brand', 'start_date', 'end_date', 'completion_status', 'log', 'pattern_name', 'pattern_designer', 'needle_size', 'needle_type')

class CrochetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crochet
        fields = ('id', 'user', 'name', 'brand', 'start_date', 'end_date', 'completion_status', 'log', 'pattern_name', 'pattern_designer', 'hook_size')

class SpinningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spinning
        fields = ('id', 'user', 'name', 'brand', 'start_date', 'end_date', 'completion_status', 'log', 'singles_weight', 'finished_yarn_weight', 'ply')

class YarnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yarn
        fields = ('id', 'user', 'name', 'brand', 'amount', 'color', 'content', 'yarn_weight', 'yardage')

class FiberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fiber
        fields = ('id', 'user', 'name', 'brand', 'amount', 'color', 'content', 'fiber_weight_grams')