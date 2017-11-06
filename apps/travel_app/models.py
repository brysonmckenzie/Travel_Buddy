# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class User(models.Model):
    first_name = models.CharField(max_length=38)
    last_name = models.CharField(max_length=38)
    user_name = models.CharField(max_length=38, unique=True)
    password = models.CharField(max_length=38)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects =  User()

class Trip(models.Model):
    destination = models.CharField(max_length=38)
    description = models.CharField(max_length=38)
    start_date = models.DateTimeField(max_length=38)
    end_date = models.DateTimeField(max_length=38)
    join = models.CharField(max_length = 8, default = 'false')
    users = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)