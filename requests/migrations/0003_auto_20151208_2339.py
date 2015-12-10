# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-09 02:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0002_auto_20151208_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacant',
            name='assigned_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vacant_assigned_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vacant',
            name='requested_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vacant_requested_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vacation',
            name='assigned_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vacation_assigned_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vacation',
            name='requested_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vacation_requested_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
