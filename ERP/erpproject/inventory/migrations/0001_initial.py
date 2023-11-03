# Generated by Django 3.2.20 on 2023-11-03 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('minqty_required', models.IntegerField()),
                ('maxqty_required', models.IntegerField()),
                ('cost_per_unit', models.FloatField()),
                ('usage_level', models.CharField(choices=[('Low level', 'Low level'), ('Mid level', 'Mid level'), ('High level', 'High level')], default='Low level', max_length=30)),
                ('reorder_duration', models.CharField(choices=[('1 week', '1 week'), ('3-4 days', '3-4 days'), ('1-2 days', '1-2 days')], default='1 week', max_length=30)),
            ],
            options={
                'db_table': 'stock_master',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=150)),
                ('location', models.CharField(max_length=100)),
                ('contact', models.BigIntegerField()),
                ('stock_name', models.CharField(max_length=100)),
                ('gst_no', models.CharField(max_length=20)),
                ('rating', models.CharField(choices=[('1 star', '1 star'), ('2 star', '2 star'), ('3 star', '3 star'), ('4 star', '4 star'), ('5 star', '5 star')], default='1 star', max_length=30)),
                ('stock_product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.stock')),
            ],
            options={
                'db_table': 'supplier_master',
            },
        ),
        migrations.AddField(
            model_name='stock',
            name='supplier_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.supplier'),
        ),
    ]
