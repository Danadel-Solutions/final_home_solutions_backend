# Generated by Django 4.0.4 on 2022-07-12 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_property_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='purpose',
            field=models.CharField(choices=[('Rent', 'rent'), ('Sale', 'forSale'), ('Shortlet', 'Shortlet'), ('Land', 'land')], default='forSale', max_length=20),
        ),
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(choices=[('Flat', 'flat'), ('Land', 'land'), ('House', 'house'), ('Commercial', 'commercial')], default='flat', max_length=20),
        ),
    ]
