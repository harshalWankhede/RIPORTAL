# Generated by Django 2.2 on 2020-02-07 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP1', '0006_auto_20200207_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='username',
            field=models.TextField(default='admin'),
        ),
    ]
