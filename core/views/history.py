from django.views.generic import TemplateView


class History(TemplateView):
    template_name = "history/index.html"
