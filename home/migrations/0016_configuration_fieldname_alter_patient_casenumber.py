# Generated by Django 4.0.2 on 2022-03-11 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_patient_casenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='fieldname',
            field=models.CharField(default=None, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='caseNumber',
            field=models.IntegerField(default=762897, unique=True, verbose_name='Case Number'),
        ),
    ]