# Generated by Django 2.2.18 on 2021-06-27 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210626_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='finishtime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='isFinished',
            field=models.BooleanField(default=False),
        ),
    ]
