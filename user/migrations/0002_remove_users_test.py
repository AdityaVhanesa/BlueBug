# Generated by Django 4.0.4 on 2022-06-16 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='test',
        ),
    ]