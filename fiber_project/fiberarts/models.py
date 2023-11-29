from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

# Create your models here.

# Project class and inheritance classes
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    completion_status = models.BooleanField(default=False)
    log = ArrayField(models.TextField(), blank=True, null=True)

    class Meta:
        abstract = True

class Knitting(Project):
    pattern_name = models.CharField(max_length=100)
    pattern_designer = models.CharField(max_length=100)
    needle_size = models.CharField(max_length=50)
    needle_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Crochet(Project):
    pattern_name = models.CharField(max_length=100)
    pattern_designer = models.CharField(max_length=100)
    hook_size = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Spinning(Project):
    singles_weight = models.CharField(max_length=20)
    finished_yarn_weight = models.CharField(max_length=20)
    ply = models.PositiveIntegerField()

    def __str__(self):
        return self.name

# Stash class and inheritance classes
class Stash(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    color = models.CharField(max_length=255)
    content = models.CharField(max_length=255)

    class Meta:
        abstract = True

class Yarn(Stash):
    yarn_weight = models.CharField(max_length=50)
    yardage = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Fiber(Stash):
    fiber_weight_grams = models.PositiveIntegerField()

    def __str__(self):
        return self.name
