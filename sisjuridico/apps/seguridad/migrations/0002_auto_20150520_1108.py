# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulos',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
