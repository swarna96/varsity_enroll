# Generated by Django 2.2.4 on 2019-08-22 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('b_date', models.DateTimeField(verbose_name='Birth Date')),
                ('roll', models.CharField(max_length=20)),
                ('dept', models.CharField(max_length=20)),
                ('session', models.CharField(max_length=20)),
            ],
        ),
    ]
