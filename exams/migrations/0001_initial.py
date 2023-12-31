# Generated by Django 4.2.7 on 2023-12-02 20:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('answer', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=1), django.core.validators.MaxValueValidator(limit_value=4)])),
                ('A', models.CharField(max_length=100)),
                ('B', models.CharField(max_length=100)),
                ('C', models.CharField(max_length=100)),
                ('D', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('level', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=1), django.core.validators.MaxValueValidator(limit_value=4)])),
                ('questions', models.ManyToManyField(related_name='exams', to='exams.question')),
            ],
        ),
    ]
