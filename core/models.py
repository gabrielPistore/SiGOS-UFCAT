from django.db import models


class Employee(models.Model):
    name: models.CharField = models.CharField(max_length=150)
    email: models.EmailField = models.EmailField()
    phone: models.CharField = models.CharField(max_length=11)

    def __str__(self):
        return self.name


class Category(models.Model):
    name: models.CharField = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class WorkOrder(models.Model):
    pass
