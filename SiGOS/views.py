from django.shortcuts import render


def new_work_order(request):
    return render(request, "SiGOS/pages/new-work-order.html")
