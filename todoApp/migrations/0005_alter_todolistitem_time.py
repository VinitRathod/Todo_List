# Generated by Django 3.2.2 on 2021-05-17 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0004_alter_todolistitem_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolistitem',
            name='time',
            field=models.TimeField(),
        ),
    ]
