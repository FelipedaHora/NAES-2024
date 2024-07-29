# Generated by Django 5.0.7 on 2024-07-29 19:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0003_alter_cidade_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=120, null=True)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('endereco', models.CharField(blank=True, max_length=255, null=True)),
                ('empresa', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=120, null=True)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('cargo', models.CharField(max_length=100)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='designers/')),
            ],
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='cidade',
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('status', models.CharField(max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Fatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_emissao', models.DateField()),
                ('data_vencimento', models.DateField()),
                ('status_pagamento', models.CharField(max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.cliente')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.projeto')),
            ],
        ),
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('data_conclusao', models.DateField(blank=True, null=True)),
                ('status', models.CharField(max_length=20)),
                ('designers', models.ManyToManyField(to='cadastros.designer')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.projeto')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentarios', models.TextField()),
                ('data_feedback', models.DateField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.cliente')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.projeto')),
                ('tarefa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cadastros.tarefa')),
            ],
        ),
        migrations.DeleteModel(
            name='Cidade',
        ),
        migrations.DeleteModel(
            name='Pessoa',
        ),
    ]