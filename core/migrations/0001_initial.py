# Generated by Django 5.0.6 on 2024-07-14 19:21

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
            name='WorkOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('department', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_phone', models.CharField(max_length=20)),
                ('landline_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('order_type', models.CharField(choices=[('type1', 'Tipo 1'), ('type2', 'Tipo 2'), ('type3', 'Tipo 3')], max_length=20)),
                ('impact', models.CharField(choices=[('low', 'Baixo'), ('medium', 'Médio'), ('high', 'Alto')], max_length=20)),
                ('urgency', models.CharField(choices=[('low', 'Baixo'), ('medium', 'Médio'), ('high', 'Alto')], max_length=20)),
                ('priority', models.CharField(choices=[('low', 'Baixo'), ('medium', 'Médio'), ('high', 'Alto')], max_length=20)),
                ('date', models.DateField()),
                ('location', models.CharField(choices=[('location1', 'Localização 1'), ('location2', 'Localização 2'), ('location3', 'Localização 3')], max_length=20)),
                ('status', models.CharField(choices=[('open', 'Aberta'), ('ongoing', 'Em andamento'), ('closed', 'Fechada')], max_length=20)),
                ('title', models.CharField(max_length=255)),
                ('report', models.CharField(max_length=500)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
                ('resposible_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.employee')),
            ],
        ),
    ]
