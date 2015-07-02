# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='historial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('equipo', models.CharField(max_length=100)),
                ('modulo', models.CharField(max_length=50)),
                ('accion', models.CharField(max_length=50)),
            ],
        ),
    ]
