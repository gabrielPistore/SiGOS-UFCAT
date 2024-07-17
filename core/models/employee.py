from django.db import models


class Employee(models.Model):
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
