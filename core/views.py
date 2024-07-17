from django.shortcuts import render

from .forms import WorkOrderForm


def home(request):
    return render(request, "core/pages/home.html")


def order_management(request):
    return render(request, "core/pages/order-management.html")


def register_work_order(request):
    form = WorkOrderForm()

    sections = {
        "personal_data": {
            "basic_info": {
                "title": "Informações Básicas",
                "fields": ["name", "department"],
            },
            "contact_info": {
                "title": "Dados para Contato",
                "fields": ["email", "mobile_phone", "landline_phone"],
            },
        },
        "request_details": {
            "data_management": {
                "title": "Dados de Gerenciamento",
                "fields": ["order_type", "category", "responsible_employee"],
            },
            "classification": {
                "title": "Critérios de Classificação",
                "fields": ["impact", "urgency", "priority"],
            },
            "work_order_info": {
                "title": "Informações da Ordem de Serviço",
                "fields": ["opening_date", "status"],
            },
            "service_info": {
                "title": "Informações de Serviço",
                "fields": ["location", "service_start_date", "service_end_date"],
            },
        },
        "detailed_report": {
            "title": "Detalhamento do Relato",
            "fields": ["report_title", "report"],
        },
    }

    return render(
        request,
        "core/pages/register-work-order.html",
        {"form": form, "sections": sections},
    )


def history(request):
    return render(request, "core/pages/history.html")
