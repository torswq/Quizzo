# Generated by Django 4.0.2 on 2022-02-09 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0002_alter_question_rightanswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='bonus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='rightAnswer',
            field=models.CharField(max_length=255),
        ),
    ]
