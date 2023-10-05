from django.db import models

# Create your models here.
class Patient(models.Model):
  name = models.CharField(max_length=200)
  birth_date = models.CharField(max_length=200)
  location = models.CharField(max_length=200)
  disease_name = models.CharField(max_length=200)

class fall(models.Model):
  data = models.CharField(max_length=100)