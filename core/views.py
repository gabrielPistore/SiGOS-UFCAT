from django.shortcuts import render

from .forms import WorkOrderForm


def home(request):
    return render(request, "core/pages/home.html")


def order_management(request):
    return render(request, "core/pages/order-management.html")


def form(request):
    form = WorkOrderForm()
    personal_data = {
        "basic_info": ["name", "department"],
        "contact_info": ["email", "mobile_phone", "landline_phone"],
    }
    request_details = {
        "data_management": ["order_type", "category", "responsible_employee"],
        "classification": ["impact", "urgency", "priority"],
        "work_order_info": ["opening_date", "status"],
        "service_info": ["location", "duration"],
    }
    return render(
        request,
        "core/pages/form.html",
        {
            "form": form,
            "personal_data": personal_data,
            "request_details": request_details,
        },
    )


def history(request):
    return render(request, "core/pages/history.html")
