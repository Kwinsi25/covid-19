# Generated by Django 3.2.5 on 2022-03-24 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_alter_patient_casenumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='block',
            old_name='fieldname',
            new_name='slug',
        ),
        migrations.AlterField(
            model_name='patient',
            name='caseNumber',
            field=models.IntegerField(default=665815, unique=True, verbose_name='Case Number'),
        ),
    ]