# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expediente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='det_exp_resolucion',
            name='ideresolucion',
        ),
        migrations.AddField(
            model_name='det_exp_resolucion',
            name='ideresolucion',
            field=models.ManyToManyField(to='expediente.resolucion'),
        ),
        migrations.RemoveField(
            model_name='det_exp_resolucion',
            name='idexpediente',
        ),
        migrations.AddField(
            model_name='det_exp_resolucion',
            name='idexpediente',
            field=models.ManyToManyField(to='expediente.expedientes'),
        ),
    ]
