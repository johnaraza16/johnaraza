# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import AppUser, Food, Foodlog, Question, WeightTracking

# Register your models here.
admin.site.register(AppUser)
admin.site.register(Food)
admin.site.register(Foodlog)
admin.site.register(Question)
admin.site.register(WeightTracking)

