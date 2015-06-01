# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('authtools', '__first__'),
        ('seguridad', '0004_remove_permisos_idperfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True, editable=False, max_length=32, blank=True)),
                ('picture', models.ImageField(upload_to='profile_pics/%Y-%m-%d/', null=True, blank=True, verbose_name='Profile picture')),
                ('bio', models.CharField(null=True, max_length=200, blank=True, verbose_name='Short Bio')),
                ('email_verified', models.BooleanField(default=False, verbose_name='Email verified')),
                ('idperfil', models.OneToOneField(to='seguridad.perfil')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
