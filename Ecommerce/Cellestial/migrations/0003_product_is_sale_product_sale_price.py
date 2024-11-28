# Generated by Django 5.1.3 on 2024-11-27 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cellestial', '0002_category_customer_product_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]