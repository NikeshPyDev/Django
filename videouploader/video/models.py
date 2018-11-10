# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models


class UserProfile(models.Model):

    user = models.OnToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_legth=20, blank=True)
    dob =  models.DateField(null=True, blank=True)
    gender = models.SmallIntegerField(choices=[(0, 'Male'), (1, 'Female')])
    phone = models.CharField()
