# Generated by Django 3.2.11 on 2022-04-09 18:32

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('helloworld', '0031_career_data_career_data_french_career_sub_data_career_sub_data_french'),
    ]

    operations = [
        migrations.CreateModel(
            name='corpo_data1',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Manage Content',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('helloworld.corpo_data',),
        ),
        migrations.CreateModel(
            name='corpo_data2',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Manage Content (French)',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('helloworld.corpo_data_french',),
        ),
        migrations.CreateModel(
            name='corpo_header1',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Manage Header',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('helloworld.corpo_header',),
        ),
        migrations.CreateModel(
            name='corpo_header2',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Manage Header (French)',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('helloworld.corpo_header_french',),
        ),
        migrations.CreateModel(
            name='corpo_sub1',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Manage Sub Content',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('helloworld.corpo_sub_data',),
        ),
        migrations.CreateModel(
            name='corpo_sub2',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Manage Sub Content (French)',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('helloworld.corpo_sub_data_french',),
        ),
    ]