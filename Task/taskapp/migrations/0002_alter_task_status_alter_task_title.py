# Generated by Django 4.1.12 on 2023-10-10 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
