# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-15 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhoneCatalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LastName', models.CharField(max_length=255)),
                ('FirstName', models.CharField(max_length=255)),
                ('Phone', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('RegDate', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.RemoveField(
            model_name='option',
            name='riddle',
        ),
        migrations.DeleteModel(
            name='Option',
        ),
        migrations.DeleteModel(
            name='Riddle',
        ),
    ]
