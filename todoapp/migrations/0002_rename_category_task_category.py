# Generated by Django 5.2.1 on 2025-06-01 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='Category',
            new_name='category',
        ),
    ]
