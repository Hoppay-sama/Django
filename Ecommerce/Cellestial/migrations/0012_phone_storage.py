# Generated by Django 5.1.3 on 2024-12-05 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cellestial', '0011_delete_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='storage',
            field=models.ManyToManyField(to='Cellestial.storage'),
        ),
    ]