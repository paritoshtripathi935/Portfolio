from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    job = models.CharField(max_length=20)
    website = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    skills = models.TextField()

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")

class experience(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")

class Bachelor(model.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    