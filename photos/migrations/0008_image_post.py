# Generated by Django 3.0 on 2020-01-07 07:56

import datetime
from django.db import migrations
from django.utils.timezone import utc
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_auto_20200107_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='post',
            field=tinymce.models.HTMLField(default=datetime.datetime(2020, 1, 7, 7, 56, 37, 798866, tzinfo=utc)),
            preserve_default=False,
        ),
    ]