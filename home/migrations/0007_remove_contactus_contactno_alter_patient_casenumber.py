# Generated by Django 4.0.2 on 2022-04-01 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_patient_casenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='contactNo',
        ),
        migrations.AlterField(
            model_name='patient',
            name='caseNumber',
            field=models.IntegerField(default=251213, unique=True, verbose_name='Case Number'),
        ),
    ]
