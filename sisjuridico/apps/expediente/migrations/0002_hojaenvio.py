# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matenimiento', '0002_auto_20150615_0934'),
        ('expediente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hojaEnvio',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('asunto', models.TextField()),
                ('observaciones', models.TextField()),
                ('fecha_emision', models.DateField()),
                ('fecha_recepcion', models.DateField()),
                ('documento_adjun', models.FileField(upload_to='HojaEnvio/%Y/%m/%d')),
                ('num_follos', models.IntegerField()),
                ('idaccion', models.ForeignKey(to='matenimiento.accion')),
                ('idexpediente', models.ForeignKey(to='expediente.expedientes')),
                ('idoficina', models.ForeignKey(to='matenimiento.oficina')),
            ],
        ),
    ]
