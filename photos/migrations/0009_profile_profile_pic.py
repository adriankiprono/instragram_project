# Generated by Django 3.0 on 2020-01-07 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0008_image_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='image2', upload_to='avatar/'),
        ),
    ]
