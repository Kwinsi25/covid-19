# Generated by Django 3.2.5 on 2022-03-23 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20220322_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='status',
            field=models.CharField(choices=[('enabled', 'Enabled'), ('disabled', 'Disabled')], default='enabled', max_length=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='caseNumber',
            field=models.IntegerField(default=736680, unique=True, verbose_name='Case Number'),
        ),
    ]
