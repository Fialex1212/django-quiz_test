# Generated by Django 5.0.3 on 2024-05-07 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0019_alter_quiz_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]
