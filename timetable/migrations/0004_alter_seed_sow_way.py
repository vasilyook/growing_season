# Generated by Django 3.2.7 on 2023-04-09 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0003_alter_seed_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seed',
            name='sow_way',
            field=models.CharField(choices=[('into_the_ground', 'into_the_ground'), ('through_seedlings', 'through_seedlings'), ('both', 'both')], max_length=20),
        ),
    ]
