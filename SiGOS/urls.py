from django.urls import path

from . import views

app_name = "SiGOS"

urlpatterns = [
    path("new-work-order/", views.new_work_order, name="new-work-order"),
]
