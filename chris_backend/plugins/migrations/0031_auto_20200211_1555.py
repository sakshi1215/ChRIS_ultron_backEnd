# Generated by Django 2.1.4 on 2020-02-11 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0030_auto_20190607_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultpathparameter',
            name='value',
            field=models.CharField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='defaultstrparameter',
            name='value',
            field=models.CharField(blank=True, max_length=600),
        ),
    ]
