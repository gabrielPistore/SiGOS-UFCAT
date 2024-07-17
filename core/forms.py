from django import forms

from utils.forms import add_placeholder, style_input_form, update_label_suffix

from .models import WorkOrder


class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            "name": "Insira seu nome",
            "department": "Insira seu departamento",
            "email": "Insira seu e-mail",
            "mobile_phone": "(DDD) 00000-0000",
            "landline_phone": "(DDD) 00000-0000",
        }

        select_fields = [
            "order_type",
            "category",
            "resposible_employee",
            "impact",
            "urgency",
            "priority",
            "status",
        ]

        for field_name, field in self.fields.items():
            # Apply a common style to all input fields
            style_input_form(field, "form-input")
            update_label_suffix(field, " ")

            # Add placeholders to specified fields
            if field_name in placeholders:
                add_placeholder(field, placeholders[field_name])

            # Add a placeholder option to select fields
            if field_name in select_fields:
                field.choices = [("", "Selecione")] + list(field.choices)

    # Personal data
    name = forms.CharField(
        label="Nome", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    department = forms.CharField(
        label="Departamento", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    email = forms.EmailField(
        label="E-mail", widget=forms.EmailInput(attrs={"class": "form-input"})
    )
    mobile_phone = forms.EmailField(
        label="Telefone Celular", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    landline_phone = forms.EmailField(
        label="Telefone Fixo (Opcional)",
        widget=forms.TextInput(attrs={"class": "form-input"}),
    )

    # Request Details
    order_type = forms.ChoiceField(label="Tipo", choices=WorkOrder.ORDER_TYPE)
    category = forms.ChoiceField(label="Categoria", widget=forms.Select())
    responsible_employee = forms.ChoiceField(
        label="Funcionário Responsável", widget=forms.Select()
    )

    impact = forms.ChoiceField(label="Impacto")
    urgency = forms.ChoiceField(label="Urgência")
    priority = forms.ChoiceField(label="Prioridade")

    opening_date = forms.DateField(
        label="Data de Abertura", widget=forms.DateInput(attrs={"type": "date"})
    )
    status = forms.ChoiceField(label="Status", choices=WorkOrder.STATUS)

    # Service Information
    location = forms.CharField(label="Localização")
    service_start_date = forms.DateField(
        label="Início do Serviço",
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    service_end_date = forms.DateField(
        label="Fim do Serviço", widget=forms.DateInput(attrs={"type": "date"})
    )

    # Detailed Report
    report_title = forms.CharField(label="Título")
    report = forms.CharField(label="Relato", widget=forms.Textarea())
