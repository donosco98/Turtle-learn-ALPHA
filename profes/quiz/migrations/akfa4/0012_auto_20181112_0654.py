# Generated by Django 2.1.3 on 2018-11-12 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_auto_20181112_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='option1_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='option2_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='option3_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
