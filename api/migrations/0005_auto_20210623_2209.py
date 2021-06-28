# Generated by Django 2.2.18 on 2021-06-23 14:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210623_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainrelation',
            name='testroom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='testroom', to='api.ClassRoom'),
        ),
        migrations.CreateModel(
            name='TestRelation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Course')),
            ],
        ),
    ]