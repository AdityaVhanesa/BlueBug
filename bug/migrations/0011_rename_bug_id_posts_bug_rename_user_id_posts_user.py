# Generated by Django 4.0.4 on 2022-07-17 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0010_rename_description_posts_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='bug_id',
            new_name='bug',
        ),
        migrations.RenameField(
            model_name='posts',
            old_name='user_id',
            new_name='user',
        ),
    ]
