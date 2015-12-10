# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Vacant(models.Model):
    def __str__(self):
        return self.requested_position

    requested_position = models.CharField(max_length=50)
    vacants_amount = models.IntegerField()
    position_type = models.IntegerField(
        choices=((1, 'Nuevo'), (2, 'Reemplazo')),
        default=1
    )
    working_day_type = models.IntegerField(
        choices=((1, 'Full-time'), (2, 'Part-time')),
        default=1
    )
    salary = models.IntegerField()
    comments = models.TextField(max_length=500)
    request_date = models.DateTimeField()
    requested_by = models.ForeignKey(User, null=True, related_name='vacant_requested_by')
    assigned_to = models.ForeignKey(User, null=True, blank=True, related_name='vacant_assigned_to')
    approved = models.BooleanField(default=False, blank=True)

class Vacation(models.Model):
    def __str__(self):
        return self.motive

    start_date = models.DateField()
    end_date = models.DateField()
    motive = models.CharField(max_length=200)
    request_date = models.DateTimeField()
    requested_by = models.ForeignKey(User, null=True, related_name='vacation_requested_by')
    assigned_to = models.ForeignKey(User, null=True, blank=True, related_name='vacation_assigned_to')