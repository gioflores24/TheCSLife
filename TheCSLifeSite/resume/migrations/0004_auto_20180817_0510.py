# Generated by Django 2.0.6 on 2018-08-17 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_resume_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='description',
            field=models.CharField(default='404 ERROR NOT FOUND', max_length=200),
        ),
    ]
