# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='apelldos',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='idperfil',
        ),
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.AddField(
            model_name='user',
            name='nombres',
            field=models.CharField(max_length=100, default=datetime.datetime(2015, 5, 31, 21, 51, 6, 100892, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
