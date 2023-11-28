from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    KNITTING = 'Knitting'
    SPINNING = 'Spinning'
    CROCHET = 'Crochet'

    PROJECT_TYPES = [
        (KNITTING, 'Knitting'),
        (SPINNING, 'Spinning'),
        (CROCHET, 'Crochet'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField()
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES, default=KNITTING)
    photo_url = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    completetion_status = models.BooleanField(default=False)
    pattern_name = models.CharField(blank=True, null=True)
    pattern_designer = models.CharField(blank=True, null=True)
    tools_used = models.TextField(blank=True, null=True)
    tools_from_stash = models.ManyToManyField('Stash', related_name='projects_using_tools', blank=True)
    yarn = models.CharField(blank=True, null=True)
    yarn_from_stash = models.ManyToManyField('Stash', related_name='projects_using_yarn', blank=True)
    fiber = models.CharField(blank=True, null=True)
    fiber_from_stash = models.ManyToManyField('Stash', related_name='projects_using_fiber', blank=True)
    plys = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.project_name

class Stash(models.Model):
    YARN = 'Yarn'
    FIBER = 'Fiber'
    TOOLS = 'Tools'

    STASH_TYPES = [
        (YARN, 'Yarn'),
        (FIBER, 'Fiber'),
        (TOOLS, 'Tools'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stash_type = models.CharField(max_length=20, choices=STASH_TYPES, default=YARN)
    item_name = models.CharField()
    photo_url = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField()
    brand = models.CharField()
    weight = models.CharField(blank=True, null=True)
    color = models.CharField(blank=True, null=True)
    content = models.CharField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    yardage = models.PositiveIntegerField(blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.item_name

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_type = models.CharField(max_length=20, choices=Project.PROJECT_TYPES)
    weekly_hours = models.DecimalField(max_digits=5, decimal_places=2)
    target_date = models.DateField()

    def __str__(self):
        return self.weekly_hours

