# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('accion', models.CharField(max_length=30)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='det_exp_resolucion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='det_hoja_exp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('fecha_emision', models.DateField()),
                ('fecha_recepcion', models.DateField()),
                ('documento_adjun', models.CharField(max_length=250)),
                ('num_follos', models.IntegerField()),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='expedientes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('asunto', models.TextField()),
                ('contenido', models.TextField()),
                ('estado', models.BooleanField(default=True)),
                ('idcategoria', models.ForeignKey(to='expediente.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='hojaEnvio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('asunto', models.TextField()),
                ('observaciones', models.TextField()),
                ('estado', models.BooleanField(default=True)),
                ('idaccion', models.ForeignKey(to='expediente.accion')),
            ],
        ),
        migrations.CreateModel(
            name='oficina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('oficina', models.CharField(max_length=30)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='resolucion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('numero', models.CharField(max_length=20)),
                ('contenido', models.CharField(max_length=100)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='hojaenvio',
            name='idoficina',
            field=models.ForeignKey(to='expediente.oficina'),
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
        migrations.AddField(
            model_name='det_exp_resolucion',
            name='ideresolucion',
            field=models.ForeignKey(to='expediente.resolucion'),
        ),
        migrations.AddField(
            model_name='det_exp_resolucion',
            name='idexpediente',
            field=models.ForeignKey(to='expediente.expedientes'),
        ),
    ]
