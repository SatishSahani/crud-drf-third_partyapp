from django.db import models

# Create your models here.
# students/models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    roll = models.IntegerField(unique=True)

    def __str__(self):
        return self.name
