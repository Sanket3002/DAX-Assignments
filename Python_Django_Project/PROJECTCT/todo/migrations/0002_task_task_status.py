# Generated by Django 4.2.3 on 2023-07-15 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_status',
            field=models.BooleanField(default=False),
        ),
    ]
