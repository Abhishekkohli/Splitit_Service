# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-12-20 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201220_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grouptransaction',
            name='debter',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='debter',
        ),
        migrations.AddField(
            model_name='grouptransaction',
            name='debtor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='transaction_debtor', to='api.SplititUser'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='debtor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.SplititUser'),
        ),
    ]
