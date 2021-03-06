# Generated by Django 3.1.3 on 2021-01-07 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0008_auto_20210105_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='mobile',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Cash On Delivery', 'Cash On Delivery'), ('Stripe', 'Stripe')], default='Cash On Delivery', max_length=200),
        ),
    ]
