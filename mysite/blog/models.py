from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField()
