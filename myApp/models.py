from django.db import models

# Create your models here.ls

class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hire_date = models.DateField()
    address = models.TextField(null=True)
    department = models.CharField(max_length=200)
    role = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

