# Generated by Django 3.0.2 on 2020-01-09 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0002_auto_20200109_1829'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phones',
            options={},
        ),
        migrations.RemoveField(
            model_name='phones',
            name='image',
        ),
    ]