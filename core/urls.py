from django.urls import path

from .views import *

app_name = "core"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("order-management/", OrderManagement.as_view(), name="order_management"),
    path("register-work-order/", register_work_order, name="register_work_order"),
    path("history/", History.as_view(), name="history"),
]
