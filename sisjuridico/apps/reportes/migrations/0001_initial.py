# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expediente', '0003_auto_20150517_1109'),
        ('seguridad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='historial',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('estado', models.BooleanField(default=True)),
                ('idexpedientes', models.ForeignKey(to='expediente.expedientes')),
                ('idpermisos', models.ForeignKey(to='seguridad.permisos')),
            ],
        ),
    ]
