# Generated by Django 2.2.18 on 2021-06-27 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20210627_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='towho',
            field=models.CharField(default='none', max_length=30),
        ),
    ]
