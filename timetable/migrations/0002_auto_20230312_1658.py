# Generated by Django 3.2.7 on 2023-03-12 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seed',
            old_name='sow_seed',
            new_name='sow_way',
        ),
        migrations.RenameField(
            model_name='seed',
            old_name='seed_type',
            new_name='type',
        ),
    ]
