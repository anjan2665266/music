# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

import re
from django.template.defaultfilters import slugify
from django.contrib.postgres.fields import ArrayField, JSONField

#import constant

class Song(models.Model):
	id = models.AutoField(primary_key=True)
	name= models.CharField(max_length=100, null=True, blank=True)
	duration_in_sec= models.IntegerField(blank=True, null=True, default=0)
	status= models.BooleanField (default=1)
	created= models.DateTimeField(auto_now_add=True)
	class Meta:
		db_table = 'project_songs'

class Podcast(models.Model):
	id = models.AutoField(primary_key=True)
	name= models.CharField(max_length=100, null=True, blank=True)
	duration_in_sec= models.IntegerField(blank=True, null=True, default=0)
	host= models.CharField(max_length=100, null=True, blank=True)
	participants = ArrayField(
            models.CharField(max_length=100, blank=True),
            size=10,
        )
	status= models.BooleanField (default=1)
	created= models.DateTimeField(auto_now_add=True)
	class Meta:
		db_table = 'project_podcast'

class Audiobook(models.Model):
	id = models.AutoField(primary_key=True)
	name= models.CharField(max_length=100, null=True, blank=True)
	author= models.CharField(max_length=100, null=True, blank=True)
	narrator= models.CharField(max_length=100, null=True, blank=True)
	duration_in_sec= models.IntegerField(blank=True, null=True, default=0)
	status= models.BooleanField (default=1)
	created= models.DateTimeField(auto_now_add=True)
	class Meta:
		db_table = 'project_audiobook'

