# Generated by Django 3.2 on 2021-04-16 17:37

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastro', '0002_auto_20210416_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=13)),
            ],
            options={
                'verbose_name': 'Stocked Product',
                'verbose_name_plural': 'Stocked products',
            },
        ),
        migrations.CreateModel(
            name='StockLocale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
                ('product_stock', models.ManyToManyField(through='stock.StockedProduct', to='cadastro.Product')),
            ],
            options={
                'verbose_name': 'Stock Locale',
                'verbose_name_plural': 'Stock Locales',
            },
        ),
        migrations.AddField(
            model_name='stockedproduct',
            name='locale',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.stocklocale'),
        ),
        migrations.AddField(
            model_name='stockedproduct',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cadastro.product'),
        ),
    ]
