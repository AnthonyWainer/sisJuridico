# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='modulos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('padre', models.CharField(max_length=10)),
                ('orden', models.IntegerField()),
                ('url', models.CharField(max_length=150)),
                ('icon', models.CharField(max_length=150)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='permisos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('buscar', models.BooleanField(default=True)),
                ('editar', models.BooleanField(default=True)),
                ('insertar', models.BooleanField(default=True)),
                ('eliminar', models.BooleanField(default=True)),
                ('imprimir', models.BooleanField(default=True)),
                ('estado', models.BooleanField(default=True)),
                ('idmodulo', models.ForeignKey(to='seguridad.modulos')),
                ('idperfil', models.ForeignKey(to='seguridad.perfil')),
                ('iduser', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
