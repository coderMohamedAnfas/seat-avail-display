from django.db import models

class College(models.Model):
    name = models.CharField(max_length=100,default="GPC PKD")

    def __str__(self):
        return self.name

class Branch(models.Model):
    college = models.ForeignKey(College, related_name='branches', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} - {self.college.name}'

class Category(models.Model):
    branch = models.ForeignKey(Branch, related_name='categories', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    availability = models.IntegerField()

    def __str__(self):
        return f'{self.branch.name} - {self.name} - {self.branch.college.name}'
