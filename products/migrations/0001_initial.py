# Generated by Django 3.0.6 on 2020-05-15 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Original',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(default='', max_length=200)),
                ('model', models.CharField(default='', max_length=300)),
                ('description', models.TextField()),
                ('build_year', models.PositiveIntegerField(default='0')),
                ('image_main', models.ImageField(upload_to='original_images')),
                ('image_two', models.ImageField(upload_to='original_images')),
                ('image_three', models.ImageField(upload_to='original_images')),
                ('status', models.CharField(choices=[('d', 'Draft'), ('h', 'Highlight'), ('a', 'Active'), ('i', 'inactive')], default='a', max_length=1)),
                ('votes', models.PositiveIntegerField(default='0')),
                ('price_min', models.DecimalField(decimal_places=2, max_digits=16)),
                ('price_max', models.DecimalField(decimal_places=2, max_digits=16)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(default='', max_length=200)),
                ('model', models.CharField(default='', max_length=300)),
                ('description', models.TextField()),
                ('scale', models.CharField(default='', max_length=60)),
                ('manufacturer', models.CharField(default='', max_length=200)),
                ('build_year', models.PositiveIntegerField(default='0')),
                ('color', models.CharField(default='', max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('promo_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image_main', models.ImageField(upload_to='product_images')),
                ('image_sec', models.ImageField(upload_to='product_images')),
                ('status', models.CharField(choices=[('p', 'Promotion'), ('s', 'Soldout'), ('o', 'Out of stock'), ('n', 'Not in sales'), ('y', 'In sales')], default='y', max_length=1)),
                ('original_key', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Original')),
            ],
        ),
    ]
