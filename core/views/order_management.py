from django.views.generic import TemplateView


class OrderManagement(TemplateView):
    template_name = "core/order_management/index.html"
