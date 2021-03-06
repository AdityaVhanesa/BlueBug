# Generated by Django 4.0.4 on 2022-07-16 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0006_alter_bugs_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bugs',
            old_name='bug_closedAt',
            new_name='closed_at',
        ),
        migrations.RenameField(
            model_name='bugs',
            old_name='bug_closedBy',
            new_name='closed_by',
        ),
        migrations.RenameField(
            model_name='bugs',
            old_name='bug_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='bugs',
            old_name='bug_foundIn',
            new_name='found_in',
        ),
        migrations.RenameField(
            model_name='bugs',
            old_name='bug_raisedBy',
            new_name='raised_by',
        ),
        migrations.RenameField(
            model_name='bugs',
            old_name='bug_severityLevel',
            new_name='severity_level',
        ),
        migrations.RenameField(
            model_name='bugs',
            old_name='bug_status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='bugs',
            old_name='bug_title',
            new_name='title',
        ),
    ]
