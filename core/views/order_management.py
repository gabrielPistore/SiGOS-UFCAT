from django.views.generic import TemplateView


class OrderManagement(TemplateView):
    template_name = "order_management/index.html"
