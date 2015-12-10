# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Vacant, Vacation

admin.site.register(Vacant)
admin.site.register(Vacation)