# Generated by Django 2.2.18 on 2021-06-25 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210623_2229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student2Relation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('grade', models.IntegerField()),
                ('mainrelation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.MainRelation')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.StudentInfo')),
            ],
        ),
    ]
