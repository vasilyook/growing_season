# Generated by Django 3.2.7 on 2023-03-12 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_auto_20230312_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seed',
            name='type',
            field=models.CharField(choices=[('flower', 'flower'), ('fruit', 'fruit'), ('herb', 'herb'), ('mushroom', 'mushroom'), ('vegetable', 'vegetable')], max_length=10),
        ),
    ]
