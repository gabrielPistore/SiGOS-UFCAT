from django.views.generic import TemplateView


class History(TemplateView):
    template_name = "core/pages/history.html"
