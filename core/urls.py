from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("order-management/", views.order_management, name="order_management"),
    path("form/", views.form, name="form"),
    path("history/", views.history, name="history"),
]
