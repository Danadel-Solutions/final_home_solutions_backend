# Generated by Django 4.0.4 on 2022-08-02 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_property_seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='api.property')),
            ],
        ),
    ]