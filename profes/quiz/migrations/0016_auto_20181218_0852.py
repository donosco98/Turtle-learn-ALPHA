# Generated by Django 2.1.3 on 2018-12-18 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0015_question_option1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='subject',
            field=models.CharField(blank=True, choices=[('Chemistry', 'Chemistry'), ('Physics', 'Physics'), ('Mathematics', 'Mathematics')], default='', max_length=90, null=True),
        ),
    ]
