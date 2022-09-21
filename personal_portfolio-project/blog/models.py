from datetime import date
from turtle import title
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200) 
    descr = models.TextField() 
    date = models.DateField() 

    def __str__(self): return self.title
     
