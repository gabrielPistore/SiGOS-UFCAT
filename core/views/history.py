from django.shortcuts import render


def history(request):
    return render(request, "core/pages/history.html")
