# Generated by Django 4.0.2 on 2022-04-01 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_patient_casenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='caseNumber',
            field=models.IntegerField(default=359770, unique=True, verbose_name='Case Number'),
        ),
    ]
