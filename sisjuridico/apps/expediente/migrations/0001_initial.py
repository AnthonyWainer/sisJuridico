# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matenimiento', '0002_auto_20150615_0934'),
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='det_hoja_exp',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('fecha_emision', models.DateField()),
                ('fecha_recepcion', models.DateField()),
                ('documento_adjun', models.CharField(max_length=250)),
                ('num_follos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='expedientes',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('fecha', models.DateField()),
                ('asunto', models.TextField()),
                ('contenido', models.TextField()),
                ('idcategoria', models.ForeignKey(to='expediente.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='hojaEnvio',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('asunto', models.TextField()),
                ('observaciones', models.TextField()),
                ('idaccion', models.ForeignKey(to='matenimiento.accion')),
                ('idoficina', models.ForeignKey(to='matenimiento.oficina')),
            ],
        ),
        migrations.CreateModel(
            name='resolucion',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('numero', models.CharField(max_length=20)),
                ('contenido', models.CharField(max_length=100)),
                ('idexpediente', models.ManyToManyField(to='expediente.expedientes')),
            ],
        ),
        migrations.AddField(
            model_name='det_hoja_exp',
            name='ideresolucion',
            field=models.ForeignKey(to='expediente.resolucion'),
        ),
        migrations.AddField(
            model_name='det_hoja_exp',
            name='idexpediente',
            field=models.ForeignKey(to='expediente.expedientes'),
        ),
        migrations.AddField(
            model_name='det_hoja_exp',
            name='idhojaenvio',
            field=models.ForeignKey(to='expediente.hojaEnvio'),
        ),
    ]
