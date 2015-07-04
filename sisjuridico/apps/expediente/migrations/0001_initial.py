# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matenimiento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='expedientes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nro', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('fecha_expediente', models.DateField()),
                ('asunto', models.TextField()),
                ('contenido', models.FileField(upload_to='Expediente/%Y/%m/%d')),
                ('estado', models.TextField()),
                ('idcategoria', models.ForeignKey(to='expediente.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='hojaEnvio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('asunto', models.TextField()),
                ('observaciones', models.TextField()),
                ('fecha_emision', models.DateField()),
                ('fecha_recepcion', models.DateField()),
                ('documento_adjun', models.FileField(upload_to='HojaEnvio/%Y/%m/%d')),
                ('num_follos', models.IntegerField()),
                ('idaccion', models.ForeignKey(to='matenimiento.accion')),
                ('idexpediente', models.ForeignKey(to='expediente.expedientes')),
                ('idoficina', models.ForeignKey(to='matenimiento.oficina')),
            ],
        ),
        migrations.CreateModel(
            name='resolucion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
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
