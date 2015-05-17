# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expediente', '0002_auto_20150517_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='det_exp_resolucion',
            name='ideresolucion',
        ),
        migrations.RemoveField(
            model_name='det_exp_resolucion',
            name='idexpediente',
        ),
        migrations.AddField(
            model_name='resolucion',
            name='idexpediente',
            field=models.ManyToManyField(to='expediente.expedientes'),
        ),
        migrations.DeleteModel(
            name='det_exp_resolucion',
        ),
    ]
