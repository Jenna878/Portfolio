from distutils.command import upload
from turtle import title
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100) 
    descr = models.CharField(max_length=250) 
    image = models.ImageField(upload_to='portfolio/images') 
    url = models.URLField(blank=True) 
   
    

