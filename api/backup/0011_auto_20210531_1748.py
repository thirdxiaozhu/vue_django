# Generated by Django 2.2.18 on 2021-05-31 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_usertoken_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentGrade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='password',
            field=models.CharField(default='123456', max_length=50, null=True),
        ),
    ]
