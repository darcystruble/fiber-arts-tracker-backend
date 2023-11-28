# Generated by Django 4.2.7 on 2023-11-28 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fiberart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.CharField(choices=[('Knitting', 'Knitting'), ('Spinning', 'Spinning'), ('Crochet', 'Crochet')], default='Knitting', max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(),
        ),
        migrations.CreateModel(
            name='Stash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stash_type', models.CharField(choices=[('Yarn', 'Yarn'), ('Fiber', 'Fiber'), ('Tools', 'Tools')], default='Yarn', max_length=20)),
                ('stash_name', models.CharField()),
                ('quantity', models.PositiveIntegerField()),
                ('brand', models.CharField()),
                ('weight', models.CharField(blank=True, null=True)),
                ('color', models.CharField(blank=True, null=True)),
                ('content', models.CharField(blank=True, null=True)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('amount', models.PositiveIntegerField()),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_type', models.CharField(choices=[('Knitting', 'Knitting'), ('Spinning', 'Spinning'), ('Crochet', 'Crochet')], max_length=20)),
                ('weekly_hours', models.DecimalField(decimal_places=2, max_digits=5)),
                ('target_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='fiber_from_stash',
            field=models.ManyToManyField(blank=True, related_name='projects_using_fiber', to='fiberart.stash'),
        ),
        migrations.AddField(
            model_name='project',
            name='tools_from_stash',
            field=models.ManyToManyField(blank=True, related_name='projects_using_tools', to='fiberart.stash'),
        ),
        migrations.AddField(
            model_name='project',
            name='yarn_from_stash',
            field=models.ManyToManyField(blank=True, related_name='projects_using_yarn', to='fiberart.stash'),
        ),
    ]
