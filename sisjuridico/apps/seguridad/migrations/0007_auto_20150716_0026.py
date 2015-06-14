# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0006_auto_20150716_0026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permisos',
            old_name='iduser',
            new_name='idperfil',
        ),
    ]
