# Generated by Django 2.2.18 on 2021-05-31 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210531_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertoken',
            name='userid',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
