# Generated by Django 3.0.5 on 2020-05-10 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('no_of_seasons', models.PositiveSmallIntegerField(default=0)),
                ('author', models.CharField(max_length=40)),
                ('rating', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('no_of_ratings', models.IntegerField(default=0)),
                ('genre', models.ManyToManyField(related_name='animes', to='anime_list.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='AnimeSeason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.PositiveSmallIntegerField()),
                ('airing', models.BooleanField()),
                ('time_of_year', models.CharField(choices=[('WIN', 'Winter'), ('SPR', 'Sprint'), ('SUM', 'Summer'), ('FAL', 'Fall')], max_length=3)),
                ('year', models.PositiveSmallIntegerField()),
                ('name_of_season', models.CharField(max_length=100)),
                ('no_of_episodes', models.IntegerField()),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seasong', to='anime_list.Anime')),
            ],
            options={
                'get_latest_by': 'season',
                'unique_together': {('anime', 'season')},
                'order_with_respect_to': 'anime',
            },
        ),
    ]
