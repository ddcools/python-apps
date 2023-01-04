from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

class User(models.Model):
  first_name = models.CharField(max_length= 255)
  last_name = models.CharField(max_length= 255)
  age = models.IntegerField()
  
  def full_name(self):
    return self.first_name + self.last_name
