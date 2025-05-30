from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
