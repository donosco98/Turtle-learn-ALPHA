# Generated by Django 2.1.3 on 2018-11-12 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_auto_20181112_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='option1_image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='option2_image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='option3_image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='option4_image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text_image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]