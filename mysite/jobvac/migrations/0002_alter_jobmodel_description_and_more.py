# Generated by Django 4.2.6 on 2023-11-05 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobvac', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobmodel',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='jobmodel',
            name='max_recommend',
            field=models.IntegerField(default=0),
        ),
    ]
