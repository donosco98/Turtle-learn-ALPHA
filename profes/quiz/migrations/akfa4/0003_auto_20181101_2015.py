# Generated by Django 2.1.3 on 2018-11-01 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20181101_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='subject',
            field=models.CharField(choices=[('maths', 'maths'), ('physics', 'physics'), ('chemistry', 'chemistry')], max_length=90),
        ),
    ]