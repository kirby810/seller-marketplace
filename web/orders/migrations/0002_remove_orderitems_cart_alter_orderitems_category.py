# Generated by Django 5.0.6 on 2024-06-20 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitems',
            name='cart',
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='category',
            field=models.CharField(max_length=20),
        ),
    ]