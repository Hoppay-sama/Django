# Generated by Django 5.1.3 on 2024-12-07 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cellestial', '0014_phone_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='hex',
            field=models.CharField(default='#000000', max_length=7),
        ),
    ]
