# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mechdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='folk',
            options={'managed': False},
        ),
    ]
