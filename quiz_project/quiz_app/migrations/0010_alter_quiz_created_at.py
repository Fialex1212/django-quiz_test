# Generated by Django 5.0.4 on 2024-04-21 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0009_alter_quiz_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='created_at',
            field=models.DateTimeField(default=21, editable=False),
        ),
    ]
