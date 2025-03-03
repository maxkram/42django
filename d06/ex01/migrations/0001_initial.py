# Generated by Django 5.1.6 on 2025-03-01 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('episode_nb', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64, unique=True)),
                ('opening_crawl', models.TextField(blank=True, null=True)),
                ('director', models.CharField(max_length=32)),
                ('producer', models.CharField(max_length=128)),
                ('release_date', models.DateField()),
            ],
            options={
                'db_table': 'ex00_schema.movies',
            },
        ),
    ]
