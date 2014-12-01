# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0002_auto_20141201_0309'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='cell_phone',
            field=localflavor.us.models.PhoneNumberField(default='612-227-2112', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='class_year',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2019)]),
            preserve_default=True,
        ),
    ]
