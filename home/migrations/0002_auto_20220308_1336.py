# Generated by Django 3.2.12 on 2022-03-08 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='patientEmail',
        ),
        migrations.AlterField(
            model_name='patient',
            name='caseNumber',
            field=models.IntegerField(default=330467, unique=True, verbose_name='Case Number'),
        ),
    ]