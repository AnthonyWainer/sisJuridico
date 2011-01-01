# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expediente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expedientes',
            name='contenido',
            field=models.FileField(upload_to='Expediente/%Y/%m/%d'),
        ),
    ]
