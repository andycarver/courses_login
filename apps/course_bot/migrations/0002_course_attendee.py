# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0001_initial'),
        ('course_bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='attendee',
            field=models.ManyToManyField(to='login_registration.User'),
        ),
    ]