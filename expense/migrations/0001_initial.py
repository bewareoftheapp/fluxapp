# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-08-19 18:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('description', models.TextField()),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='Reimburse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expense.Budget')),
            ],
        ),
    ]
