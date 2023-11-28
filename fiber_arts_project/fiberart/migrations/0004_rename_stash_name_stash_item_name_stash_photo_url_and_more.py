# Generated by Django 4.2.7 on 2023-11-28 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiberart', '0003_remove_stash_amount_stash_yardage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stash',
            old_name='stash_name',
            new_name='item_name',
        ),
        migrations.AddField(
            model_name='stash',
            name='photo_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='photo_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='tools_used',
            field=models.TextField(blank=True, null=True),
        ),
    ]