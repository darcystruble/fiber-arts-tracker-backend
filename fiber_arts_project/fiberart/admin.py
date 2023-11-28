from django.contrib import admin
from .models import Project, Stash, Goal

# Register your models here.
admin.site.register(Project)
admin.site.register(Stash)
admin.site.register(Goal)