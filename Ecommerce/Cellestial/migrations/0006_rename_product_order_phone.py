# Generated by Django 5.1.3 on 2024-11-28 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cellestial', '0005_color_storage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='product',
            new_name='phone',
        ),
    ]