from __future__ import unicode_literals

from django.db import models

class Gods(models.Model):
	god_name = models.CharField(max_length = 30)
	god_type = models.CharField(max_length = 15)
	god_class = models.CharField(max_length = 30)
	god_image = models.CharField(max_length = 150)

class Roles(models.Model): 
	role_name = models.CharField(max_length = 15)
	role_gods = models.ManyToManyField(Gods)