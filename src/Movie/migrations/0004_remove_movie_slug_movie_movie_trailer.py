# Generated by Django 4.1 on 2022-08-28 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0003_movie_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='slug',
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_trailer',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
