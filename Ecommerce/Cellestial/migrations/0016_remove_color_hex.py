# Generated by Django 5.1.3 on 2024-12-07 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cellestial', '0015_color_hex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='hex',
        ),
    ]
