# Generated by Django 5.0.4 on 2024-04-27 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0012_alter_answer_id_alter_question_id_alter_quiz_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]