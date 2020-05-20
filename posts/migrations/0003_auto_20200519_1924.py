# Generated by Django 3.0.6 on 2020-05-19 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200519_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('m', 'Moderate'), ('p', 'Published'), ('s', 'Suspended')], default='m', max_length=1),
        ),
    ]
