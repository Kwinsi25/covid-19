# Generated by Django 4.0.2 on 2022-03-03 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_staff_staffphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='staffPhoto',
            field=models.ImageField(blank=True, null=True, upload_to='staffImages'),
        ),
    ]