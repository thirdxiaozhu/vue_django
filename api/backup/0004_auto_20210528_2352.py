# Generated by Django 2.2.18 on 2021-05-28 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210526_0022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentinfo',
            old_name='entryTime',
            new_name='entrytime',
        ),
        migrations.RenameField(
            model_name='teacherinfo',
            old_name='entryTime',
            new_name='entrytime',
        ),
    ]
