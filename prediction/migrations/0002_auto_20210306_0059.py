# Generated by Django 3.0.2 on 2021-03-06 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='lower_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='prediction',
            name='upper_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
