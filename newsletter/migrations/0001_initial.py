# Generated by Django 3.2 on 2023-03-20 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('conf_num', models.CharField(max_length=15)),
                ('confirmed', models.BooleanField(default=False)),
            ],
        ),
    ]
