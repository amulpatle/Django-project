# Generated by Django 5.0.2 on 2024-03-07 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_candidate_country_candidate_experience_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='Descriptionn',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.CharField(default='', max_length=150),
        ),
    ]
