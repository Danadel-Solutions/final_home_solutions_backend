# Generated by Django 4.0.4 on 2022-05-02 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_title', models.CharField(max_length=250)),
                ('second_title', models.CharField(max_length=250)),
                ('cover_photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
