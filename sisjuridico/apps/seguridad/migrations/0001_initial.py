# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('usuario', models.CharField(unique=True, max_length=50)),
                ('email', models.EmailField(unique=True, max_length=50)),
                ('nombres', models.CharField(null=True, max_length=100)),
                ('apellidos', models.CharField(null=True, max_length=100)),
                ('dni', models.CharField(null=True, max_length=20)),
                ('telefono', models.IntegerField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', to='auth.Group', related_name='user_set', blank=True, related_query_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='modulos',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('padre', models.IntegerField()),
                ('url', models.CharField(max_length=150)),
                ('icon', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='permisos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('ver', models.BooleanField(default=True)),
                ('buscar', models.BooleanField(default=True)),
                ('editar', models.BooleanField(default=True)),
                ('insertar', models.BooleanField(default=True)),
                ('eliminar', models.BooleanField(default=True)),
                ('imprimir', models.BooleanField(default=True)),
                ('idmodulo', models.ForeignKey(to='seguridad.modulos')),
                ('idperfil', models.ForeignKey(to='seguridad.perfil')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='idperfil',
            field=models.ForeignKey(null=True, to='seguridad.perfil'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(verbose_name='user permissions', help_text='Specific permissions for this user.', to='auth.Permission', related_name='user_set', blank=True, related_query_name='user'),
        ),
    ]
