# Generated by Django 2.2.11 on 2020-05-14 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_cart_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
