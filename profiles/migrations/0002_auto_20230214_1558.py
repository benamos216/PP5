# Generated by Django 3.2 on 2023-02-14 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_last_name',
        ),
    ]