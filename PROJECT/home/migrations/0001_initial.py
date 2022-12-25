# Generated by Django 3.2.11 on 2022-02-20 22:02

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('helloworld', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Manage Home Page Content',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('helloworld.home_content',),
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Modify Hero',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('helloworld.hero_text',),
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Modify Logo',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('helloworld.brand_text',),
        ),
    ]
