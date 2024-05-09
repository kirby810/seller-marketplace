# Generated by Django 5.0.3 on 2024-05-09 02:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seller_product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField(default=0)),
                ('payment_total_price', models.IntegerField(default=0)),
                ('amount', models.SmallIntegerField(default=0)),
                ('order_date', models.DateField()),
                ('payment_date', models.DateField()),
                ('pay_confirm', models.BooleanField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='seller_product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
