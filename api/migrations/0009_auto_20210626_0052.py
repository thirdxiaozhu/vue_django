# Generated by Django 2.2.18 on 2021-06-26 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_student2relation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student2relation',
            name='grade',
            field=models.IntegerField(null=True),
        ),
    ]
