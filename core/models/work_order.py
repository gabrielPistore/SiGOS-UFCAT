from django.db import models

from .category import Category
from .employee import Employee


class WorkOrder(models.Model):
    class Meta:
        verbose_name = "Work Order"
        verbose_name_plural = "Work Orders"

    # Personal data
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    mobile_phone = models.CharField(max_length=20)
    landline_phone = models.CharField(max_length=20, blank=True, null=True)

    LEVEL = [
        ("low", "Baixa"),
        ("medium", "Média"),
        ("high", "Alta"),
    ]

    # Work Order Details
    ORDER_TYPE = [
        ("type1", "Tipo 1"),
        ("type2", "Tipo 2"),
        ("type3", "Tipo 3"),
    ]
    IMPACT = LEVEL
    URGENCY = LEVEL
    PRIORITY = LEVEL
    STATUS = [
        ("open", "Aberta"),
        ("ongoing", "Em andamento"),
        ("closed", "Fechada"),
    ]
    order_type = models.CharField(max_length=20, choices=ORDER_TYPE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    responsible_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    impact = models.CharField(max_length=20, choices=IMPACT)
    urgency = models.CharField(max_length=20, choices=URGENCY)
    priority = models.CharField(max_length=20, choices=PRIORITY)
    opening_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS)
    location = models.CharField(max_length=255)
    service_start_date = models.DateField(blank=True, null=True)
    service_end_date = models.DateField(blank=True, null=True)

    # Report
    report_title = models.CharField(max_length=255)
    report = models.CharField(max_length=500)

    def __str__(self):
        return f"Order de Serviço {self.id}"
