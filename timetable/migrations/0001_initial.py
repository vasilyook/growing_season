# Generated by Django 3.2.7 on 2023-03-12 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sow_seed', models.CharField(choices=[('into_the_ground', 'into_the_ground'), ('through_seedlings', 'through_seedlings')], max_length=20)),
                ('seed_type', models.CharField(choices=[('flower', 'flower'), ('fruit', 'fruit'), ('herb', 'herb'), ('mushroom', 'mushroom')], max_length=10)),
                ('image', models.CharField(max_length=200)),
                ('stratification', models.BooleanField()),
                ('sow_start', models.CharField(max_length=100)),
                ('sow_end', models.CharField(max_length=100)),
                ('expired_on', models.DateField()),
            ],
        ),
    ]
