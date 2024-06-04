from django.shortcuts import render


def home(request):
    return render(request, "core/pages/home.html")


def order_management(request):
    return render(request, "core/pages/order-management.html")


def form(request):
    return render(request, "core/pages/form.html")


def history(request):
    return render(request, "core/pages/history.html")
