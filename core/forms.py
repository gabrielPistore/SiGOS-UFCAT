from django import forms

from utils.forms import add_placeholder

from .models import WorkOrder


class WorkOrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields["name"], "Insira seu nome")
        add_placeholder(self.fields["department"], "Insira seu departamento")
        add_placeholder(self.fields["email"], "Insira seu e-mail")
        add_placeholder(self.fields["mobile_phone"], "(DDD) 00000-0000")
        add_placeholder(self.fields["landline_phone"], "(DDD) 00000-0000")

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

    class Meta:
        model = WorkOrder
        fields = "__all__"
