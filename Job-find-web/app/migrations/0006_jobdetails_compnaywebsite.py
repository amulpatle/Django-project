# Generated by Django 5.0.2 on 2024-03-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_jobdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdetails',
            name='compnaywebsite',
            field=models.CharField(default='', max_length=250),
        ),
    ]
