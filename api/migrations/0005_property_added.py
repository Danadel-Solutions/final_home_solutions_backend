# Generated by Django 4.0.4 on 2022-05-06 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_property_location_property_price_property_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='added',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
