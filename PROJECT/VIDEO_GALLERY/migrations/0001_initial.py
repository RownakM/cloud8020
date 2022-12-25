# Generated by Django 3.2.11 on 2022-02-20 22:02

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('helloworld', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='video',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('helloworld.videogallery',),
        ),
        migrations.CreateModel(
            name='video_data',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Video Info',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('helloworld.videodata',),
        ),
    ]