# Generated by Django 2.2.18 on 2021-06-27 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20210627_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='messagetype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.MessageType'),
        ),
    ]
