# seatavailability/models.py
from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    branch = models.ForeignKey(Branch, related_name='categories', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    availability = models.IntegerField()

    def __str__(self):
        return f'{self.branch.name} - {self.name}'
