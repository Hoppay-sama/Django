# Generated by Django 5.1.3 on 2024-11-22 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Album', '0003_album_image_alter_album_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.ImageField(blank=True, default='0.png', upload_to=''),
        ),
    ]