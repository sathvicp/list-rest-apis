# Generated by Django 3.0.5 on 2020-05-10 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animeseason',
            name='no_of_episodes',
            field=models.PositiveIntegerField(),
        ),
    ]
