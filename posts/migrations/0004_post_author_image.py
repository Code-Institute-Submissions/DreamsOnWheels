# Generated by Django 3.0.6 on 2020-05-19 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200519_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_image',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]