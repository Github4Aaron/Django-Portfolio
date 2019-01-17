from django.db import models

# Create your models here.

class Job(models.Model):
  
  image = models.ImageField(upload_to='images/')
  summary = models.CharField(max_length=200)

  # Migrations will create a table with rows and columns
  #  This should be done whenever a new model is made or changes to a model
  # python3 manage.py makemigrations
