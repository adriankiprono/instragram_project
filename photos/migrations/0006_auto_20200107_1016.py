# Generated by Django 3.0 on 2020-01-07 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_auto_20200107_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Profile'),
        ),
    ]
