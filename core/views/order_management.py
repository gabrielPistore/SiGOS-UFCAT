from django.shortcuts import render


def order_management(request):
    return render(request, "core/pages/order-management.html")
