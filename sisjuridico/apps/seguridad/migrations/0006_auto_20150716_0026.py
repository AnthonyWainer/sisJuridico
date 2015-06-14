# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0005_remove_permisos_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permisos',
            name='iduser',
            field=models.ForeignKey(to='seguridad.perfil'),
        ),
    ]
