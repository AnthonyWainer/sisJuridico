# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0003_auto_20150602_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulos',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
