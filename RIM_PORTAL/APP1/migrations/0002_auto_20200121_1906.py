# Generated by Django 2.2 on 2020-01-21 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='offer',
            new_name='show',
        ),
        migrations.AlterField(
            model_name='issue',
            name='incidents',
            field=models.TextField(),
        ),
    ]
