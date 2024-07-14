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


class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class WorkOrder(models.Model):
    class Meta:
        verbose_name = "Work Order"
        verbose_name = "Work Orders"

    # Personal data
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    mobile_phone = models.CharField(max_length=20)
    landline_phone = models.CharField(max_length=20, blank=True, null=True)

    # Work Order Details
    ORDER_TYPE = [
        ("type1", "Tipo 1"),
        ("type2", "Tipo 2"),
        ("type3", "Tipo 3"),
    ]
    IMPACT = [
        ("low", "Baixo"),
        ("medium", "Médio"),
        ("high", "Alto"),
    ]
    URGENCY = [
        ("low", "Baixo"),
        ("medium", "Médio"),
        ("high", "Alto"),
    ]
    PRIORITY = [
        ("low", "Baixo"),
        ("medium", "Médio"),
        ("high", "Alto"),
    ]
    LOCATION = [
        ("location1", "Localização 1"),
        ("location2", "Localização 2"),
        ("location3", "Localização 3"),
    ]
    STATUS = [
        ("open", "Aberta"),
        ("ongoing", "Em andamento"),
        ("closed", "Fechada"),
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
    title = models.CharField(max_length=255)
    report = models.CharField(max_length=500)

    def __str__(self):
        return f"Order de Serviço {self.id}"
