# Generated by Django 5.1 on 2024-08-28 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pet',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('species', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female')], max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('price', models.FloatField()),
                ('is_activate', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'pet',
            },
        ),
    ]
