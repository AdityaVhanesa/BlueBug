# Generated by Django 4.0.4 on 2022-06-16 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0002_alter_bugs_options_bugs_bug_status_bugs_closed_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bugs',
            options={'get_latest_by': 'uuid', 'ordering': ['uuid']},
        ),
        migrations.RenameField(
            model_name='bugs',
            old_name='bug_description',
            new_name='description',
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
        migrations.RenameField(
            model_name='bugs',
            old_name='bug_id',
            new_name='uuid',
        ),
    ]
