# Generated by Django 3.2.12 on 2022-03-08 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20220308_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='caseNumber',
            field=models.IntegerField(default=924819, unique=True, verbose_name='Case Number'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patientEmail',
            field=models.EmailField(max_length=254, verbose_name='Email Id'),
        ),
    ]
