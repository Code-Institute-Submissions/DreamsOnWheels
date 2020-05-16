# Generated by Django 3.0.6 on 2020-05-16 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200516_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='original',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('h', 'Highlight'), ('a', 'Active'), ('i', 'Inactive')], default='a', max_length=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(blank=True, decimal_places=2, default='0.0', max_digits=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('p', 'Promotion'), ('s', 'Soldout'), ('o', 'Out of stock'), ('n', 'Not on sales'), ('y', 'On sales')], default='y', max_length=1),
        ),
    ]