# Generated by Django 2.2.18 on 2021-05-25 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Countries'),
        ),
    ]