# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0004_auto_20150531_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='idperfil',
            field=models.ForeignKey(to='seguridad.perfil', null=True),
        ),
    ]
