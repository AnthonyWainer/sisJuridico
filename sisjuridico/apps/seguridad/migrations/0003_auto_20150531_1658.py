# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0002_auto_20150531_1651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='apelldos',
            new_name='apellidos',
        ),
    ]
