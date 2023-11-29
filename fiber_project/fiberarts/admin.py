from django.contrib import admin
from .models import Knitting, Crochet, Spinning, Yarn, Fiber

# Register your models here.
admin.site.register(Knitting)
admin.site.register(Crochet)
admin.site.register(Spinning)
admin.site.register(Yarn)
admin.site.register(Fiber)
