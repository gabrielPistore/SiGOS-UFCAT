from django.views.generic import TemplateView

from core.forms import WorkOrderForm


class WorkOrderFormView(TemplateView):
    template_name = "core/work_order_form/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = WorkOrderForm()

        sections = [
            {
                "title": "Dados Pessoais",
                "sections": [
                    {
                        "title": "Informações Básicas",
                        "fields": ["name", "department"],
                    },
                    {
                        "title": "Dados para Contato",
                        "fields": ["email", "mobile_phone", "landline_phone"],
                    },
                ],
            },
            {
                "title": "Detalhes da Solicitação",
                "sections": [
                    {
                        "title": "Dados de Gerenciamento",
                        "fields": ["order_type", "category", "responsible_employee"],
                    },
                    {
                        "title": "Critérios de Classificação",
                        "fields": ["impact", "urgency", "priority"],
                    },
                    {
                        "title": "Informações da Ordem de Serviço",
                        "fields": ["opening_date", "status"],
                    },
                    {
                        "title": "Informações de Serviço",
                        "fields": [
                            "location",
                            "service_start_date",
                            "service_end_date",
                        ],
                    },
                ],
            },
            {
                "title": "Detalhamento do Relato",
                "sections": [
                    {
                        "title": "Relato",
                        "fields": ["report_title", "report"],
                    },
                ],
            },
        ]

        context.update({"form": form, "sections": sections})
        return context
