# Generated by Django 2.1.3 on 2018-12-17 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_test_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='time',
            field=models.IntegerField(default=3600),
        ),
    ]
