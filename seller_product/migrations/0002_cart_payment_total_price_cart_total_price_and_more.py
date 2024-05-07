# Generated by Django 5.0.4 on 2024-05-07 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller_product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='payment_total_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='total_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]