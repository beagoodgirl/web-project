# Generated by Django 3.1.2 on 2021-12-08 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonus', '0006_auto_20211207_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='prize',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
