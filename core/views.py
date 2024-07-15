from django.shortcuts import render

from .forms import WorkOrderForm


def home(request):
    return render(request, "core/pages/home.html")


def order_management(request):
    return render(request, "core/pages/order-management.html")


def form(request):
    form = WorkOrderForm()

    # Personal data
    personal_data = {
        "basic_info": ["name", "department"],
        "contact_info": ["email", "mobile_phone", "landline_phone"],
    }

    return render(
        request,
        "core/pages/form.html",
        {
            "form": form,
            "personal_data": personal_data,
        },
    )


def history(request):
    return render(request, "core/pages/history.html")
