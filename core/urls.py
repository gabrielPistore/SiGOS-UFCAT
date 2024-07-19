from django.urls import path

from .views import *

app_name = "core"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("order-management/", OrderManagement.as_view(), name="order_management"),
    path("work-order-form/", WorkOrderFormView.as_view(), name="work_order_form"),
    path("history/", History.as_view(), name="history"),
]
