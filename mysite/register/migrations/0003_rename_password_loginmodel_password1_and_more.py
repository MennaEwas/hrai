# Generated by Django 4.2.6 on 2023-10-30 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_alter_loginmodel_options_remove_loginmodel_created_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loginmodel',
            old_name='password',
            new_name='password1',
        ),
        migrations.AddField(
            model_name='loginmodel',
            name='password2',
            field=models.CharField(default='default_password_value', max_length=100),
        ),
    ]