# Generated by Django 3.1.6 on 2021-02-03 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210202_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('entrees', 'entrees'), ('treats', 'treats'), ('appetizers', 'appetizers'), ('drinks', 'drinks')], max_length=60),
        ),
    ]
