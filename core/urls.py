from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("order-management/", views.order_management, name="order_management"),
    path("register-work-order/", views.register_work_order, name="register_work_order"),
    path("history/", views.history, name="history"),
]
