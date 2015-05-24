# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('authtools', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL)),
                ('slug', models.SlugField(max_length=32, blank=True, unique=True, editable=False)),
                ('picture', models.ImageField(upload_to='profile_pics/%Y-%m-%d/', blank=True, null=True, verbose_name='Profile picture')),
                ('bio', models.CharField(max_length=200, blank=True, null=True, verbose_name='Short Bio')),
                ('email_verified', models.BooleanField(default=False, verbose_name='Email verified')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
