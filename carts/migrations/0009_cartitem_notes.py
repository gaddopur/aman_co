# Generated by Django 2.2.11 on 2020-05-17 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0008_auto_20200516_0742'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
