# Generated by Django 5.0.7 on 2024-07-12 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_contactus_contactno_alter_patient_casenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='caseNumber',
            field=models.IntegerField(default=635821, unique=True, verbose_name='Case Number'),
        ),
    ]
