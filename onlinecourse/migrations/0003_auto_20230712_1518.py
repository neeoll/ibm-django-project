# Generated by Django 3.1.3 on 2023-07-12 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_submission_choice_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='choice_id',
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_id',
            field=models.IntegerField(default=0),
        ),
    ]
