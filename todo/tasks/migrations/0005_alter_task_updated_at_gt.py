# Generated by Django 4.0.3 on 2022-04-30 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_updated_at_gt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='updated_at_gt',
            field=models.DateTimeField(),
        ),
    ]
