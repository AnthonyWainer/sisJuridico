# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0001_initial'),
        ('reportes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historial',
            name='idpermisos',
            field=models.ForeignKey(to='seguridad.permisos'),
        ),
    ]
