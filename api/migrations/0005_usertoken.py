# Generated by Django 2.2.18 on 2021-05-31 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210528_2352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usertoken',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=64)),
            ],
        ),
    ]
