# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-28 13:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cm1', '0003_auto_20170324_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tempcontactotheraccount',
            name='temp_contact',
        ),
        migrations.AlterModelOptions(
            name='tempcontact',
            options={'ordering': ('-updated_at',), 'verbose_name_plural': 'Temporary Contacts'},
        ),
        migrations.AlterModelOptions(
            name='tempcontactemail',
            options={'verbose_name_plural': 'Temporary Contact Emails'},
        ),
        migrations.AlterModelOptions(
            name='tempcontactnickname',
            options={'verbose_name_plural': 'Contacts NickName'},
        ),
        migrations.AlterModelOptions(
            name='tempcontactphone',
            options={'verbose_name_plural': 'Temporary Contact Phones'},
        ),
        migrations.AlterModelOptions(
            name='tempcontactsocialaccount',
            options={'verbose_name_plural': 'Temporary Contact Social Accounts'},
        ),
        migrations.AlterModelOptions(
            name='tempcontactwebsite',
            options={'verbose_name_plural': 'Temporary Contact Websites'},
        ),
        migrations.AlterUniqueTogether(
            name='tempcontactemail',
            unique_together=set([('temp_contact', 'email_address')]),
        ),
        migrations.AlterUniqueTogether(
            name='tempcontactphone',
            unique_together=set([('temp_contact', 'country_code', 'phone_number')]),
        ),
        migrations.DeleteModel(
            name='TempContactOtherAccount',
        ),
    ]
