# Generated by Django 5.1.2 on 2024-10-16 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.TextField(blank=True, max_length=100, null=True)),
                ('category_img', models.ImageField(blank=True, null=True, upload_to='category')),
            ],
        ),
    ]
