# Generated by Django 2.1.3 on 2018-11-22 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20181115_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='response',
            field=models.CharField(blank=True, default='option5', max_length=90, null=True),
        ),
    ]
