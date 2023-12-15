# Generated by Django 4.2.7 on 2023-12-15 14:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='level',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)]),
        ),
    ]
