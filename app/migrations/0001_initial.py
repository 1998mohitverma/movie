# Generated by Django 3.0 on 2023-03-25 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=70)),
                ('thumbnail', models.TextField()),
                ('director_name', models.CharField(max_length=50)),
                ('release_year', models.IntegerField()),
                ('movie_rating', models.FloatField()),
            ],
        ),
    ]
