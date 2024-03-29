# Generated by Django 5.0.2 on 2024-03-07 07:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_descriptionn_company_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobname', models.CharField(max_length=250)),
                ('companyname', models.CharField(max_length=250)),
                ('companyaddress', models.CharField(max_length=250)),
                ('jobdescription', models.CharField(max_length=250)),
                ('qualification', models.CharField(max_length=250)),
                ('responsibility', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('companyemail', models.CharField(max_length=250)),
                ('companycontact', models.CharField(max_length=250)),
                ('salarypackage', models.CharField(max_length=250)),
                ('experience', models.CharField(max_length=250)),
                ('logo', models.ImageField(default='', upload_to='app/img/jobpost')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
            ],
        ),
    ]
