# Generated by Django 4.1.4 on 2022-12-12 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_record'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='authorId',
        ),
        migrations.AlterField(
            model_name='record',
            name='data',
            field=models.TextField(),
        ),
    ]