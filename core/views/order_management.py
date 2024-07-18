from django.views.generic import TemplateView


class OrderManagement(TemplateView):
    template_name = "core/pages/order-management.html"
