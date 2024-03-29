# Generated by Django 2.2.11 on 2020-05-09 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0004_auto_20200508_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('products', models.ManyToManyField(blank=True, null=True, to='products.Product')),
            ],
        ),
    ]
