from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=200)
	sid = models.IntegerField()
	
	
def publish(self):
        self.published_date = timezone.now()
        self.save()

 
def __str__(self):
	return self.name
