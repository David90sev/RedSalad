# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 02:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import usuarios.models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario_blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuerpo', models.CharField(max_length=150)),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Entrada_Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('cuerpo', models.CharField(max_length=2500)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to=usuarios.models.get_image_path)),
                ('fecha', models.DateTimeField()),
                ('productor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Productor')),
            ],
        ),
        migrations.AddField(
            model_name='comentario_blog',
            name='entrada_blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Entrada_Blog'),
        ),
        migrations.AddField(
            model_name='comentario_blog',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario'),
        ),
    ]