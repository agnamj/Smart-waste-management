# Generated by Django 5.1.2 on 2024-10-18 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adonaiapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=100, null=True)),
                ('pro_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('Mrp', models.IntegerField(blank=True, null=True)),
                ('Description', models.TextField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('manufactured', models.CharField(blank=True, max_length=100, null=True)),
                ('category_image1', models.ImageField(blank=True, null=True, upload_to='product')),
                ('category_image2', models.ImageField(blank=True, null=True, upload_to='product')),
                ('category_image3', models.ImageField(blank=True, null=True, upload_to='product')),
            ],
        ),
    ]
