# Generated by Django 2.1.7 on 2021-12-07 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonus', '0004_auto_20211207_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='winner',
            name='week',
            field=models.CharField(default='1', max_length=1),
        ),
    ]
