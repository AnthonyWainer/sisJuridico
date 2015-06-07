# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0004_auto_20150602_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permisos',
            name='estado',
        ),
    ]
