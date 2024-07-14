# Generated by Django 5.0.6 on 2024-07-14 05:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('report', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('department', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_phone', models.CharField(max_length=20)),
                ('landline_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('order_type', models.CharField(choices=[('type1', 'Type 1'), ('type2', 'Type 2'), ('type3', 'Type 3')], max_length=20)),
                ('impact', models.CharField(choices=[('baixo', 'Baixo'), ('medio', 'Médio'), ('alto', 'Alto')], max_length=20)),
                ('urgency', models.CharField(choices=[('baixo', 'Baixo'), ('medio', 'Médio'), ('alto', 'Alto')], max_length=20)),
                ('priority', models.CharField(choices=[('baixo', 'Baixo'), ('medio', 'Médio'), ('alto', 'Alto')], max_length=20)),
                ('date', models.DateField()),
                ('location', models.CharField(choices=[('localicao1', 'Localização 1'), ('localicao2', 'Localização 2'), ('localicao3', 'Localização 3')], max_length=20)),
                ('status', models.CharField(choices=[('aberta', 'Aberta'), ('em_andamento', 'Em andamento'), ('fechada', 'Fechada')], max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.report')),
                ('resposible_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.employee')),
            ],
        ),
    ]
