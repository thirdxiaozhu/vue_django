# Generated by Django 2.2.18 on 2021-06-22 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_mainrelation_stuquantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainRelation2Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Course')),
            ],
        ),
        migrations.AlterField(
            model_name='mainrelation',
            name='student',
            field=models.ManyToManyField(through='api.MainRelation2Student', to='api.StudentInfo'),
        ),
        migrations.AddField(
            model_name='mainrelation2student',
            name='mainrelation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.MainRelation'),
        ),
        migrations.AddField(
            model_name='mainrelation2student',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.StudentInfo'),
        ),
        migrations.AlterUniqueTogether(
            name='mainrelation2student',
            unique_together={('mainrelation', 'student')},
        ),
    ]