from django.views.generic import TemplateView


class History(TemplateView):
    template_name = "core/history/index.html"
