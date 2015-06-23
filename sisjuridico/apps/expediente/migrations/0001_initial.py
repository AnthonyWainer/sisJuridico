# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='expedientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nro', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('fecha_expediente', models.DateField()),
                ('asunto', models.TextField()),
                ('contenido', models.FileField(upload_to='Expediente/%Y/%m/%d')),
                ('idcategoria', models.ForeignKey(to='expediente.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='resolucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('numero', models.CharField(max_length=20)),
                ('contenido', models.FileField(upload_to='Resolucion/%Y/%m/%d')),
            ],
        ),
        migrations.AddField(
            model_name='expedientes',
            name='idresolucion',
            field=models.ManyToManyField(to='expediente.resolucion'),
        ),
    ]
