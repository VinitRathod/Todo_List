# Generated by Django 3.2.2 on 2021-05-17 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0003_todolistitem_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolistitem',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
