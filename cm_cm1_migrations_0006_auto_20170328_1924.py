# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-28 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cm1', '0005_tempcontactotheraccount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempcontact',
            name='other_phone',
            field=models.IntegerField(null=True),
        ),
    ]
