# Generated by Django 4.2.6 on 2023-10-31 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Announcement_id', models.CharField(max_length=100)),
                ('Company_id', models.CharField(max_length=100)),
                ('Creator', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('is_published', models.BooleanField(default=False)),
                ('is_remote', models.BooleanField(default=False)),
                ('max_recommend', models.IntegerField()),
                ('position_name', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['Announcement_id'],
            },
        ),
    ]
