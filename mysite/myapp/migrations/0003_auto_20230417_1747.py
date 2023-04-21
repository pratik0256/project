# Generated by Django 3.2.18 on 2023-04-17 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20230413_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSVData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Index', models.IntegerField(default=0)),
                ('M2_Declaration_Number', models.CharField(max_length=255)),
                ('CIF_Value', models.FloatField()),
                ('Stat_Quantity', models.FloatField()),
                ('COMMODITY_DESC', models.CharField(max_length=255)),
                ('GOODS_DESCRIPTION', models.CharField(max_length=255)),
                ('unit_price', models.FloatField()),
                ('Test', models.CharField(max_length=255)),
                ('Test2', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='csv_data',
        ),
    ]
