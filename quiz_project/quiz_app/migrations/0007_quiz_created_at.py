# Generated by Django 5.0.4 on 2024-04-21 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0006_alter_userprofile_options_likequiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
