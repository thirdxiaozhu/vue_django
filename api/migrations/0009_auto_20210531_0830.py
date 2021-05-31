# Generated by Django 2.2.18 on 2021-05-31 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210531_0829'),
    ]

    operations = [
        migrations.AddField(
            model_name='admininfo',
            name='token',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Usertoken'),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='token',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Usertoken'),
        ),
        migrations.AddField(
            model_name='teacherinfo',
            name='token',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Usertoken'),
        ),
    ]
