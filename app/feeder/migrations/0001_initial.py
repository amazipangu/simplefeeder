# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 12:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=500)),
                ('link', models.URLField()),
                ('created_at', models.DateTimeField(verbose_name='created_at')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('created_at', models.DateTimeField(verbose_name='created at')),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeder.Service'),
        ),
    ]
