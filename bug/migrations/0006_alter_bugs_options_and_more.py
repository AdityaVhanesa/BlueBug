# Generated by Django 4.0.4 on 2022-07-16 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0005_alter_bugs_closed_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bugs',
            options={'get_latest_by': 'id', 'ordering': ['id']},
        ),
        migrations.RenameField(
            model_name='bugs',
            old_name='closed_at',
            new_name='bug_closedAt',
        ),
        migrations.RenameField(
            model_name='bugs',
            old_name='closed_by',
            new_name='bug_closedBy',
        ),
        migrations.RenameField(
            model_name='bugs',
            old_name='description',
            new_name='bug_description',
        ),
        migrations.RenameField(
            model_name='bugs',
            old_name='raised_by',
            new_name='bug_raisedBy',
        ),
        migrations.RenameField(
            model_name='bugs',
            old_name='status',
            new_name='bug_status',
        ),
        migrations.RenameField(
            model_name='bugs',
            old_name='title',
            new_name='bug_title',
        ),
        migrations.RemoveField(
            model_name='bugs',
            name='uuid',
        ),
        migrations.AddField(
            model_name='bugs',
            name='bug_foundIn',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bugs',
            name='bug_severityLevel',
            field=models.CharField(default='LEVEL - 3', max_length=50),
        ),
    ]