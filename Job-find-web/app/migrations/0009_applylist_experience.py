# Generated by Django 5.0.2 on 2024-03-09 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_applylist'),
    ]

    operations = [
        migrations.AddField(
            model_name='applylist',
            name='experience',
            field=models.CharField(default='', max_length=100),
        ),
    ]
