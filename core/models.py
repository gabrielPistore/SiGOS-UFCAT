from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Report(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    report = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class WorkOrder(models.Model):
    # Personal data
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    mobile_phone = models.CharField(max_length=20)
    landline_phone = models.CharField(max_length=20, blank=True, null=True)

    # Work Order Details
    ORDER_TYPE = [
        ("type1", "Type 1"),
        ("type2", "Type 2"),
        ("type3", "Type 3"),
    ]
    IMPACT = [
        ("baixo", "Baixo"),
        ("medio", "Médio"),
        ("alto", "Alto"),
    ]
    URGENCY = [
        ("baixo", "Baixo"),
        ("medio", "Médio"),
        ("alto", "Alto"),
    ]
    PRIORITY = [
        ("baixo", "Baixo"),
        ("medio", "Médio"),
        ("alto", "Alto"),
    ]
    LOCATION = [
        ("localicao1", "Localização 1"),
        ("localicao2", "Localização 2"),
        ("localicao3", "Localização 3"),
    ]
    STATUS = [
        ("aberta", "Aberta"),
        ("em_andamento", "Em andamento"),
        ("fechada", "Fechada"),
    ]

    order_type = models.CharField(max_length=20, choices=ORDER_TYPE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    resposible_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    impact = models.CharField(max_length=20, choices=IMPACT)
    urgency = models.CharField(max_length=20, choices=URGENCY)
    priority = models.CharField(max_length=20, choices=PRIORITY)
    date = models.DateField()
    location = models.CharField(max_length=20, choices=LOCATION)
    status = models.CharField(max_length=20, choices=STATUS)

    # Report
    report = models.ForeignKey(Report, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order de Serviço {self.id}"
