# Generated by Django 4.1.1 on 2022-09-17 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0002_drink_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='img',
            field=models.ImageField(default='', upload_to='../my-app'),
        ),
    ]