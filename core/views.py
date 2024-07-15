from django.shortcuts import render

from .forms import WorkOrderForm


def home(request):
    return render(request, "core/pages/home.html")


def order_management(request):
    return render(request, "core/pages/order-management.html")


def form(request):
    form = WorkOrderForm()
    return render(
        request,
        "core/pages/form.html",
        {"form": form},
    )


def history(request):
    return render(request, "core/pages/history.html")
